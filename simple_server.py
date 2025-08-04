#!/usr/bin/env python3
"""
Simple HTTP server for Railway deployment
Uses Python's built-in http.server - no external dependencies
"""

import os
import http.server
import socketserver
import json
from urllib.parse import urlparse

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"LearnNest Enhanced is running!")
            
        elif path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'status': 'healthy', 'message': 'App is running'})
            self.wfile.write(response.encode())
            
        elif path == '/healthcheck':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            
        elif path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"pong")
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Not Found")

def main():
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting simple server on port {port}")
    
    with socketserver.TCPServer(("", port), SimpleHandler) as httpd:
        print(f"Server running on port {port}")
        httpd.serve_forever()

if __name__ == '__main__':
    main() 