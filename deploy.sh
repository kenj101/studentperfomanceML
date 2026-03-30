#!/bin/bash
# Production deployment script for Student Performance Prediction App

echo "🚀 Starting Student Performance Prediction App with Gunicorn..."

# Configuration
WORKERS=4
HOST=0.0.0.0
PORT=8000
APP_MODULE=app:app

# Start Gunicorn
gunicorn \
    --workers $WORKERS \
    --bind $HOST:$PORT \
    --log-level info \
    --access-logfile - \
    --error-logfile - \
    $APP_MODULE

echo "✅ App deployed at http://$HOST:$PORT"