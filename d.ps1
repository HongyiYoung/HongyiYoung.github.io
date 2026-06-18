$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   Starting Source Backup & Deployment" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# ---------------------------------------------------------
# Step 1: Pull from Remote to Sync
# ---------------------------------------------------------
Write-Host "`n[1] Pulling latest changes from 'source' branch..." -ForegroundColor Yellow
try {
    git pull origin source
} catch {
    Write-Host "  -> Pull failed! Please resolve conflicts manually." -ForegroundColor Red
    exit 1
}
Write-Host "  -> Source is up to date." -ForegroundColor Green

# ---------------------------------------------------------
# Step 2: Commit local changes
# ---------------------------------------------------------
Write-Host "`n[2] Committing local changes..." -ForegroundColor Yellow
git add .

$time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$msg = "Backup & Deploy: $time"
if ($args.Length -gt 0) {
    $msg = $args[0]
}

try {
    git commit -m $msg | Out-Null
    Write-Host "  -> Committed successfully: $msg" -ForegroundColor Green
} catch {
    Write-Host "  -> Nothing to commit (working tree clean)." -ForegroundColor Gray
}

# ---------------------------------------------------------
# Step 3: Push to Remote (Triggers GH Actions Deploy)
# ---------------------------------------------------------
Write-Host "`n[3] Pushing to remote 'source' branch..." -ForegroundColor Yellow
git push -u origin source

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n========================================================" -ForegroundColor Cyan
    Write-Host " ✅ All Done! " -ForegroundColor Green
    Write-Host " GitHub Actions will automatically build and deploy the site." -ForegroundColor Cyan
    Write-Host " Source code is backed up to the 'source' branch." -ForegroundColor Cyan
    Write-Host " You can safely switch devices and pull from 'source'!" -ForegroundColor Cyan
    Write-Host "========================================================" -ForegroundColor Cyan
} else {
    Write-Host "  -> Push failed! Check network/credentials." -ForegroundColor Red
}

Read-Host "Press Enter to exit..."
