# PowerShell script to clean up old log files in a directory
# Usage: .\cleanup_logs.ps1 -Path "C:\path\to\logs" -Days 30
param(
    [string]$Path = ".",
    [int]$Days = 30
)

$cutoff = (Get-Date).AddDays(-$Days)

Get-ChildItem -Path $Path -Recurse -Include *.log |
    Where-Object { $_.LastWriteTime -lt $cutoff } |
    ForEach-Object {
        Write-Host "Deleting $_.FullName"
        Remove-Item $_.FullName -Force
    }

Write-Host "Log cleanup complete."
