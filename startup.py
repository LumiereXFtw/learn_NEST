#!/usr/bin/env python3
"""
Simple startup script for LearnNest Enhanced
"""

import os
import sys
from app import app

def main():
    """Initialize and start the application"""
    try:
        # Initialize database lazily
        from app import init_db
        print("📊 Initializing database...")
        init_db()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"⚠️ Database initialization failed: {e}")
        print("🚀 Continuing without database initialization...")
    
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

if __name__ == '__main__':
    main() 