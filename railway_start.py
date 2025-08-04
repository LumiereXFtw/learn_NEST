#!/usr/bin/env python3
"""
Railway startup script for LearnNest Enhanced
Handles database initialization and proper app startup
"""

import os
import sys
from app import app, init_db

def main():
    """Initialize database and start the Flask app"""
    try:
        print("🚀 Starting LearnNest Enhanced on Railway...")
        
        # Initialize database
        print("📊 Initializing database...")
        init_db()
        print("✅ Database initialized successfully")
        
        # Get port from Railway environment
        port = int(os.environ.get('PORT', 5000))
        
        print(f"🌐 Starting server on port {port}")
        print("🎯 LearnNest Enhanced is ready!")
        
        # Start the Flask app
        app.run(
            host='0.0.0.0',
            port=port,
            debug=False
        )
        
    except Exception as e:
        print(f"❌ Error starting LearnNest: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 