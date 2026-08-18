$ErrorActionPreference = "Stop"
$project = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $project

if (-not (Test-Path ".venv\Scripts\python.exe")) {
    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) {
        py -3.11 -m venv .venv
    } else {
        python -m venv .venv
    }
}

$python = ".\.venv\Scripts\python.exe"

& $python -m pip install --upgrade pip
& $python -m pip install -r requirements.txt

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
}

& $python -m pytest -v
if ($LASTEXITCODE -ne 0) {
    throw "Tests failed. API will not start."
}

Write-Host ""
Write-Host "Tests passed." -ForegroundColor Green
Write-Host "Swagger: http://127.0.0.1:8000/docs"
Write-Host "Dashboard in second terminal: .\run_dashboard.ps1"

& $python -m uvicorn app.main:app --port 8000
