#!/usr/bin/env python3
"""
Main entry point for LearnNest Enhanced on Railway
This file serves as the WSGI application entry point
"""

import os
import sys

# Import Flask app first
from app import app

# Create the WSGI application
application = app

if __name__ == '__main__':
    # Get port from Railway environment
    port = int(os.environ.get('PORT', 5000))
    
    print(f"🌐 Starting server on port {port}")
    print("🎯 LearnNest Enhanced is ready!")
    
    # Start the Flask app
    application.run(
        host='0.0.0.0',
        port=port,
        debug=False
    ) 