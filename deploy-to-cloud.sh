# Deploy script for GitHub + Cloud
# Run this before pushing to GitHub for deployment

echo "🚀 Preparing for cloud deployment..."

# Train models if not exists
if [ ! -f "models.pkl" ]; then
    echo "📊 Training ML models..."
    python model.py
fi

# Add all files
echo "📁 Adding files to git..."
git add .

# Commit
echo "💾 Committing changes..."
git commit -m "Deploy: Add trained models and deployment config"

# Push
echo "⬆️ Pushing to GitHub..."
git push origin main

echo "✅ Ready for cloud deployment!"
echo "🌐 Your app will be live at your cloud provider's URL"