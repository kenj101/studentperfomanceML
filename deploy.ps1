# Production deployment script for Student Performance Prediction App
# Run with: .\deploy.ps1

Write-Host "🚀 Starting Student Performance Prediction App with Waitress..." -ForegroundColor Green

# Configuration
$HOST = "0.0.0.0"
$PORT = 8000
$THREADS = 4

# Start Waitress
waitress-serve --host $HOST --port $PORT --threads $THREADS app:app

Write-Host "✅ App deployed at http://$HOST`:$PORT" -ForegroundColor Green