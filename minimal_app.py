#!/usr/bin/env python3
"""
Minimal Flask app for Railway deployment
This bypasses all potential startup issues
"""

from flask import Flask, jsonify

# Create minimal Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "LearnNest Enhanced is running!"

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'App is running'})

@app.route('/healthcheck')
def healthcheck():
    return "OK", 200

@app.route('/ping')
def ping():
    return "pong", 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting minimal app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False) 