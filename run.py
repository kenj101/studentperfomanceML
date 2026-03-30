#!/usr/bin/env python3
"""
Production deployment script for Student Performance Prediction App
"""

import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from app import app

if __name__ == '__main__':
    # Get port from environment variable (for cloud deployment)
    port = int(os.environ.get('PORT', 8000))

    # Production settings
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,
        threaded=True
    )