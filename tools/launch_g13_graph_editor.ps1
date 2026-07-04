[CmdletBinding()]
param(
    [ValidateSet("Menu", "Staging", "Refresh", "Live", "Status")]
    [string]$Mode = "Menu",
    [ValidateRange(1024, 65535)]
    [int]$Port = 8765,
    [switch]$CheckOnly,
    [switch]$NoBrowser
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Python = Join-Path $RepoRoot ".venv\Scripts\python.exe"
$GraphCli = Join-Path $RepoRoot "tools\g13_graph.py"
$Editor = Join-Path $RepoRoot "tools\g13_graph_editor.py"
$Sources = Join-Path $RepoRoot "data\sources.json"
$GraphRoot = Join-Path $env:USERPROFILE "GitDirs\gurney-genealogy-g13-graph"
$LiveDb = Join-Path $GraphRoot "g13-context.sqlite"
$LiveExport = Join-Path $RepoRoot "data\context-graphs\g13\exports"
$LiveRecovery = Join-Path $LiveExport "current.ndjson"
$StagingDb = Join-Path $GraphRoot "g13-staging.sqlite"
$StagingExport = Join-Path $GraphRoot "staging-exports"
$Url = "http://127.0.0.1:$Port/"
$WasMenu = $Mode -eq "Menu"

function Write-Heading {
    param([string]$Text)
    Write-Host ""
    Write-Host $Text -ForegroundColor Cyan
}

function Assert-File {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "$Label was not found: $Path"
    }
}

function Invoke-Graph {
    param(
        [string[]]$Arguments,
        [int[]]$AllowedExitCodes = @(0)
    )
    $output = & $Python $GraphCli @Arguments 2>&1
    $exitCode = $LASTEXITCODE
    $text = ($output | ForEach-Object { "$_" }) -join [Environment]::NewLine
    if ($AllowedExitCodes -notcontains $exitCode) {
        throw "Graph command failed (exit $exitCode):`n$text"
    }
    return $text
}

function Get-GraphStatus {
    param([string]$Database, [string]$ExportDirectory)
    $json = Invoke-Graph @(
        "--db", $Database,
        "--export-dir", $ExportDirectory,
        "--sources", $Sources,
        "status"
    )
    return $json | ConvertFrom-Json
}

function Show-GraphStatus {
    param([string]$Label, $Status)
    Write-Host ("{0,-11} revision {1}; recovery {2}; snapshot {3}; indexes {4}; validation {5}" -f
        $Label,
        $Status.database_revision,
        $Status.recovery_state,
        $Status.snapshot_state,
        $Status.derived_index_state,
        $Status.validation_state)
}

function Restore-Staging {
    Assert-File $LiveRecovery "Live recovery export"
    Write-Host "Creating staging from the current live recovery export..."
    Invoke-Graph @(
        "--db", $StagingDb,
        "--export-dir", $StagingExport,
        "--sources", $Sources,
        "restore", "--from", $LiveRecovery
    ) | Out-Null
}

function Refresh-Staging {
    $expectedDb = [IO.Path]::GetFullPath((Join-Path $GraphRoot "g13-staging.sqlite"))
    $expectedExport = [IO.Path]::GetFullPath((Join-Path $GraphRoot "staging-exports"))
    if (
        [IO.Path]::GetFullPath($StagingDb) -ne $expectedDb -or
        [IO.Path]::GetFullPath($StagingExport) -ne $expectedExport
    ) {
        throw "Refusing to refresh unexpected staging paths."
    }

    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $archive = Join-Path $GraphRoot "staging-archive\$stamp"
    New-Item -ItemType Directory -Path $archive -Force | Out-Null

    Write-Host "Archiving the current staging pair to:"
    Write-Host "  $archive"
    foreach ($path in @($StagingDb, "$StagingDb-wal", "$StagingDb-shm", "$StagingDb-journal")) {
        if (Test-Path -LiteralPath $path -PathType Leaf) {
            Move-Item -LiteralPath $path -Destination $archive
        }
    }
    if (Test-Path -LiteralPath $StagingExport -PathType Container) {
        Move-Item -LiteralPath $StagingExport -Destination (Join-Path $archive "staging-exports")
    }

    try {
        Restore-Staging
    }
    catch {
        throw "Staging refresh failed. The previous staging database and exports remain safe in $archive.`n$($_.Exception.Message)"
    }
}

function Repair-DerivedState {
    param(
        [string]$Database,
        [string]$ExportDirectory,
        [string]$Label
    )
    $status = Get-GraphStatus $Database $ExportDirectory
    if ($status.source_registry_state -ne "current") {
        throw "$Label source registry is not current. Review and run sync-sources before opening the editor."
    }
    if ($status.derived_index_state -ne "current") {
        Write-Host "$Label FTS indexes are $($status.derived_index_state); rebuilding..."
        Invoke-Graph @(
            "--db", $Database,
            "--export-dir", $ExportDirectory,
            "--sources", $Sources,
            "reindex"
        ) | Out-Null
    }
    $status = Get-GraphStatus $Database $ExportDirectory
    if ($status.recovery_state -ne "current") {
        Write-Host "$Label recovery export is $($status.recovery_state); refreshing..."
        Invoke-Graph @(
            "--db", $Database,
            "--export-dir", $ExportDirectory,
            "--sources", $Sources,
            "export", "--recovery"
        ) | Out-Null
    }

    $validationJson = Invoke-Graph @(
        "--db", $Database,
        "--export-dir", $ExportDirectory,
        "--sources", $Sources,
        "validate"
    ) @(0, 1)
    $validation = $validationJson | ConvertFrom-Json
    if (-not $validation.valid) {
        $errors = @($validation.issues | Where-Object { $_.severity -eq "error" })
        $message = ($errors | ForEach-Object {
            "  [$($_.code)] $($_.record_id): $($_.message)"
        }) -join [Environment]::NewLine
        throw "$Label validation failed:`n$message"
    }
    return Get-GraphStatus $Database $ExportDirectory
}

function Get-RunningEditorStatus {
    try {
        return Invoke-RestMethod -Uri ($Url + "api/status") -TimeoutSec 1
    }
    catch {
        return $null
    }
}

function Test-PortOccupied {
    $client = New-Object System.Net.Sockets.TcpClient
    try {
        $task = $client.ConnectAsync("127.0.0.1", $Port)
        return $task.Wait(400) -and $client.Connected
    }
    catch {
        return $false
    }
    finally {
        $client.Dispose()
    }
}

try {
    Write-Host "G13 Context Graph Editor" -ForegroundColor Green
    Write-Host "Repository: $RepoRoot"

    Assert-File $Python "Repository Python environment"
    Assert-File $GraphCli "Graph CLI"
    Assert-File $Editor "Graph editor"
    Assert-File $Sources "Source registry"
    Assert-File $LiveDb "Live graph database"
    Assert-File $LiveRecovery "Live recovery export"

    $pythonVersion = & $Python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "The repository Python environment did not start."
    }
    Write-Host "Environment: $pythonVersion"

    if ($Mode -eq "Menu") {
        Write-Heading "Choose a database"
        Write-Host "  1  Staging / test copy (safe default)"
        Write-Host "  2  Refresh staging from live, then open it"
        Write-Host "  3  Live / production database (writes are real)"
        Write-Host "  4  Show status only"
        Write-Host "  Q  Quit"
        $choice = Read-Host "Choice [1]"
        if ([string]::IsNullOrWhiteSpace($choice)) {
            $choice = "1"
        }
        switch ($choice.Trim().ToUpperInvariant()) {
            "1" { $Mode = "Staging" }
            "2" { $Mode = "Refresh" }
            "3" { $Mode = "Live" }
            "4" { $Mode = "Status" }
            "Q" { exit 0 }
            default { throw "Unknown menu choice: $choice" }
        }
    }

    if ($Mode -eq "Status") {
        Write-Heading "Graph status"
        Show-GraphStatus "Live" (Get-GraphStatus $LiveDb $LiveExport)
        if (Test-Path -LiteralPath $StagingDb -PathType Leaf) {
            Show-GraphStatus "Staging" (Get-GraphStatus $StagingDb $StagingExport)
        }
        else {
            Write-Host "Staging     not created"
        }
        exit 0
    }

    if ($Mode -eq "Live") {
        Write-Host ""
        Write-Host "LIVE MODE can change the canonical graph and its live recovery export." -ForegroundColor Yellow
        $confirmation = Read-Host "Type LIVE to continue"
        if ($confirmation -cne "LIVE") {
            Write-Host "Live launch cancelled."
            exit 0
        }
        $Database = $LiveDb
        $ExportDirectory = $LiveExport
        $Label = "Live"
    }
    else {
        $Database = $StagingDb
        $ExportDirectory = $StagingExport
        $Label = "Staging"
    }

    $running = Get-RunningEditorStatus
    if ($null -ne $running) {
        if ($Mode -eq "Refresh") {
            throw "An editor is already running on port $Port. Stop it before refreshing staging."
        }
        if ([IO.Path]::GetFullPath($running.database_path) -eq [IO.Path]::GetFullPath($Database)) {
            if ($Mode -eq "Staging") {
                $liveStatus = Get-GraphStatus $LiveDb $LiveExport
                if ($running.database_revision -lt $liveStatus.database_revision) {
                    Write-Host "The running staging editor is revision $($running.database_revision); live is revision $($liveStatus.database_revision)." -ForegroundColor Yellow
                    Write-Host "Stop the existing editor with Ctrl+C, relaunch, and choose Refresh staging to see the current live data."
                    if ($WasMenu) {
                        $openOld = Read-Host "Open the older running staging editor anyway? [y/N]"
                        if ($openOld.Trim() -notmatch "^[Yy]") {
                            exit 0
                        }
                    }
                }
            }
            Write-Host "The requested editor is already running. Opening it now."
            if (-not $NoBrowser) {
                Start-Process $Url
            }
            exit 0
        }
        throw "Port $Port already hosts the editor for $($running.database_path). Stop it before opening another mode."
    }
    if (Test-PortOccupied) {
        throw "Port $Port is already in use by another program. Close it or launch with -Port <number>."
    }

    if ($Mode -eq "Refresh") {
        Refresh-Staging
        $Mode = "Staging"
    }
    elseif ($Mode -eq "Staging" -and -not (Test-Path -LiteralPath $StagingDb -PathType Leaf)) {
        Restore-Staging
    }

    if ($Mode -eq "Staging" -and $WasMenu) {
        $liveStatus = Get-GraphStatus $LiveDb $LiveExport
        $stagingStatus = Get-GraphStatus $StagingDb $StagingExport
        if ($stagingStatus.database_revision -lt $liveStatus.database_revision) {
            Write-Host ""
            Write-Host "Staging is revision $($stagingStatus.database_revision); live is revision $($liveStatus.database_revision)." -ForegroundColor Yellow
            $refresh = Read-Host "Archive staging and refresh it from live? [Y/n]"
            if ([string]::IsNullOrWhiteSpace($refresh) -or $refresh.Trim() -match "^[Yy]") {
                Refresh-Staging
            }
            else {
                Write-Host "Keeping the older staging copy."
            }
        }
    }

    Write-Heading "$Label preflight"
    $status = Repair-DerivedState $Database $ExportDirectory $Label
    Show-GraphStatus $Label $status
    if ($status.validation_warnings -gt 0) {
        Write-Host "Validation has $($status.validation_warnings) warning(s); the editor will show details." -ForegroundColor Yellow
    }

    if ($CheckOnly) {
        Write-Host "Preflight complete; server launch skipped (-CheckOnly)."
        exit 0
    }

    Write-Heading "Starting $Label editor"
    Write-Host "URL: $Url"
    Write-Host "Close with Ctrl+C in this window."

    $browserJob = $null
    if (-not $NoBrowser) {
        $browserJob = Start-Job -ArgumentList $Url -ScriptBlock {
            param($TargetUrl)
            for ($attempt = 0; $attempt -lt 40; $attempt++) {
                try {
                    Invoke-WebRequest -Uri $TargetUrl -UseBasicParsing -TimeoutSec 1 | Out-Null
                    Start-Process $TargetUrl
                    return
                }
                catch {
                    Start-Sleep -Milliseconds 250
                }
            }
        }
    }

    $editorArguments = @(
        $Editor,
        "--db", $Database,
        "--export-dir", $ExportDirectory,
        "--sources", $Sources,
        "--port", "$Port"
    )
    if ($Mode -eq "Live") {
        $editorArguments += "--allow-live"
    }
    try {
        & $Python @editorArguments
        if ($LASTEXITCODE -ne 0) {
            throw "The editor server exited with code $LASTEXITCODE."
        }
    }
    finally {
        if ($null -ne $browserJob) {
            if ($browserJob.State -eq "Running") {
                Stop-Job $browserJob
            }
            Receive-Job $browserJob -ErrorAction SilentlyContinue | Out-Null
            Remove-Job $browserJob -Force
        }
    }
}
catch {
    Write-Host ""
    Write-Host "Launch failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
