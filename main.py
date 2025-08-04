#!/usr/bin/env python3
"""
Main entry point for LearnNest Enhanced on Railway
This file serves as the WSGI application entry point
"""

import os
import sys
from app import app, init_db

def main():
    """Initialize database and return the Flask app"""
    try:
        print("🚀 Initializing LearnNest Enhanced...")
        
        # Initialize database
        print("📊 Initializing database...")
        init_db()
        print("✅ Database initialized successfully")
        
        return app
        
    except Exception as e:
        print(f"❌ Error initializing LearnNest: {e}")
        sys.exit(1)

# Create the WSGI application
application = main()

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