#!/usr/bin/env python3
"""
Hybrid server that starts simple but loads full app functionality
"""

import os
import sys
import threading
import time
import http.server
import socketserver
import json
from urllib.parse import urlparse

class HybridHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.full_app_loaded = False
        self.full_app = None
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Always respond to health checks immediately
        if path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"pong")
            return
            
        if path == '/healthcheck':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            return
            
        if path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'status': 'healthy', 'message': 'App is running'})
            self.wfile.write(response.encode())
            return
        
        # For all other requests, try to use full app if loaded
        if hasattr(self, 'full_app') and self.full_app:
            try:
                # Use the full Flask app
                from werkzeug.test import EnvironBuilder
                from werkzeug.wrappers import Request
                
                builder = EnvironBuilder(path=path, method='GET')
                environ = builder.get_environ()
                request = Request(environ)
                
                with self.full_app.request_context(request):
                    response = self.full_app.full_dispatch_request()
                    self.send_response(response.status_code)
                    for header, value in response.headers:
                        self.send_header(header, value)
                    self.end_headers()
                    self.wfile.write(response.get_data())
                return
            except Exception as e:
                print(f"Full app request failed: {e}")
        
        # Fallback to simple response
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"LearnNest Enhanced is starting... Please wait a moment and refresh.")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"App is starting... Please wait.")

def load_full_app():
    """Load the full Flask app in a separate thread"""
    global full_app_loaded, full_app
    
    try:
        print("🔄 Loading full LearnNest application...")
        
        # Import the full app
        from app import app, init_db
        
        # Initialize database
        print("📊 Initializing database...")
        init_db()
        print("✅ Database initialized successfully")
        
        # Store the app globally
        global full_app
        full_app = app
        full_app_loaded = True
        
        print("✅ Full LearnNest application loaded successfully!")
        
    except Exception as e:
        print(f"❌ Failed to load full app: {e}")
        print("⚠️ Continuing with simple server only")

def main():
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Starting hybrid server on port {port}")
    
    # Start loading the full app in background
    print("🔄 Starting background app loading...")
    app_thread = threading.Thread(target=load_full_app, daemon=True)
    app_thread.start()
    
    # Create handler class with full app reference
    class HandlerWithApp(HybridHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.full_app = None
        
        def do_GET(self):
            # Check if full app is loaded
            if full_app_loaded and full_app:
                self.full_app = full_app
            super().do_GET(*args, **kwargs)
    
    # Start the server
    with socketserver.TCPServer(("", port), HandlerWithApp) as httpd:
        print(f"🌐 Server running on port {port}")
        print("📡 Health checks will work immediately")
        print("🔄 Full app loading in background...")
        httpd.serve_forever()

if __name__ == '__main__':
    main() 