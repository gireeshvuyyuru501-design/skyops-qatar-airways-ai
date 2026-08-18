$ErrorActionPreference = "Stop"
$project = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $project

$python = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    throw ".venv not found. Run run_all.ps1 first."
}

& $python -m streamlit run dashboard.py
