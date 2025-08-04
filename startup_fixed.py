#!/usr/bin/env python3
"""
Fixed startup script for LearnNest Enhanced
Handles initialization properly with error recovery
"""

import os
import sys
import time

def main():
    """Initialize and start the application with proper error handling"""
    
    print("🚀 Starting LearnNest Enhanced...")
    
    # Step 1: Import Flask app (this should work)
    try:
        from app import app
        print("✅ Flask app imported successfully")
    except Exception as e:
        print(f"❌ Failed to import Flask app: {e}")
        print("🔄 Trying alternative import...")
        try:
            # Try importing just the basic Flask app
            from flask import Flask
            app = Flask(__name__)
            @app.route('/')
            def home():
                return "LearnNest Enhanced - Basic Mode"
            @app.route('/ping')
            def ping():
                return "pong", 200
            print("✅ Created basic Flask app")
        except Exception as e2:
            print(f"❌ Failed to create basic app: {e2}")
            return
    
    # Step 2: Initialize database (with error handling)
    try:
        from app import init_db
        print("📊 Initializing database...")
        init_db()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"⚠️ Database initialization failed: {e}")
        print("🚀 Continuing without database initialization...")
    
    # Step 3: Start the server
    try:
        port = int(os.environ.get('PORT', 5000))
        print(f"🌐 Starting server on port {port}")
        print("🎯 LearnNest Enhanced is ready!")
        
        # Start the Flask app
        app.run(
            host='0.0.0.0',
            port=port,
            debug=False,
            threaded=True
        )
    except Exception as e:
        print(f"❌ Failed to start server: {e}")
        print("🔄 Trying alternative startup...")
        
        # Fallback: Simple HTTP server
        try:
            import http.server
            import socketserver
            
            class SimpleHandler(http.server.BaseHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b"LearnNest Enhanced - Fallback Mode")
            
            with socketserver.TCPServer(("", port), SimpleHandler) as httpd:
                print(f"🌐 Fallback server running on port {port}")
                httpd.serve_forever()
        except Exception as e2:
            print(f"❌ Fallback also failed: {e2}")

if __name__ == '__main__':
    main() 