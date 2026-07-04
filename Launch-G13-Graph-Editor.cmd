@echo off
setlocal
cd /d "%~dp0"

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass ^
  -File "%~dp0tools\launch_g13_graph_editor.ps1" %*

set "exit_code=%ERRORLEVEL%"
if not "%exit_code%"=="0" (
  echo.
  echo The G13 graph editor launcher stopped with an error.
  echo Review the message above, then press any key to close this window.
  pause >nul
)
exit /b %exit_code%
