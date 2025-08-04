#!/usr/bin/env python3
"""
Main entry point for LearnNest Enhanced on Railway
This file serves as the WSGI application entry point
"""

import os
import sys

# Import Flask app first
from app import app

# Initialize database in a separate function to avoid startup delays
def initialize_app():
    try:
        from app import init_db
        print("🚀 Initializing LearnNest Enhanced...")
        print("📊 Initializing database...")
        init_db()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing LearnNest: {e}")
        # Don't exit, let the app start anyway

# Create the WSGI application
application = app

# Initialize database when the module is loaded
initialize_app()

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