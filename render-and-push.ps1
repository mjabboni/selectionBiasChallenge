# Render and Push Script
# This script renders the Quarto document and commits/pushes changes to git

Write-Host "[*] Rendering Quarto document..." -ForegroundColor Cyan
quarto render index.qmd

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] Render completed successfully!" -ForegroundColor Green
    
    Write-Host "`n[*] Adding changes to git..." -ForegroundColor Cyan
    git add .
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $commitMessage = "Auto-commit after render: $timestamp"
    
    Write-Host "[*] Committing changes..." -ForegroundColor Cyan
    git commit -m $commitMessage
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[*] Pushing to remote repository..." -ForegroundColor Cyan
        git push
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`n[+] Successfully rendered, committed, and pushed!" -ForegroundColor Green
        } else {
            Write-Host "`n[!] Push failed. Please check your remote configuration." -ForegroundColor Yellow
        }
    } else {
        Write-Host "`n[!] No changes to commit or commit failed." -ForegroundColor Yellow
    }
} else {
    Write-Host "`n[-] Render failed. Not committing or pushing." -ForegroundColor Red
    exit 1
}

