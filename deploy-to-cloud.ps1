# Deploy script for GitHub + Cloud
# Run this before pushing to GitHub for deployment

Write-Host "🚀 Preparing for cloud deployment..." -ForegroundColor Green

# Train models if not exists
if (!(Test-Path "models.pkl")) {
    Write-Host "📊 Training ML models..." -ForegroundColor Yellow
    python model.py
}

# Add all files
Write-Host "📁 Adding files to git..." -ForegroundColor Blue
git add .

# Commit
Write-Host "💾 Committing changes..." -ForegroundColor Blue
git commit -m "Deploy: Add trained models and deployment config"

# Push
Write-Host "⬆️ Pushing to GitHub..." -ForegroundColor Blue
git push origin main

Write-Host "✅ Ready for cloud deployment!" -ForegroundColor Green
Write-Host "🌐 Your app will be live at your cloud provider's URL" -ForegroundColor Cyan