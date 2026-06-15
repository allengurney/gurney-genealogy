@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0bootstrap_python_toolchain.ps1" %*
