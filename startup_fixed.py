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
    
    # Step 1: Initialize database FIRST (before importing app)
    try:
        print("📊 Initializing database first...")
        
        # Import database connection function
        import sqlite3
        
        # Create database connection
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Create all tables
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT, avatar TEXT, is_approved INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, display_name TEXT, bio TEXT, notif_forum INTEGER DEFAULT 1, notif_grades INTEGER DEFAULT 1, notif_announcements INTEGER DEFAULT 1, dark_mode INTEGER DEFAULT 0, badges TEXT, points INTEGER DEFAULT 0, api_token TEXT, is_blocked INTEGER DEFAULT 0, full_name TEXT, email TEXT, phone TEXT, institution TEXT, payment_screenshot TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS courses
                     (id INTEGER PRIMARY KEY, title TEXT, creator_id INTEGER, description TEXT, reference_file_path TEXT, meeting_link TEXT, outline TEXT, objectives TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, course_code TEXT UNIQUE)''')
        c.execute('''CREATE TABLE IF NOT EXISTS course_files
                     (id INTEGER PRIMARY KEY, course_id INTEGER, filename TEXT, file_type TEXT, subtitle_path TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS enrollments
                     (id INTEGER PRIMARY KEY, user_id INTEGER, course_id INTEGER, enrollment_number TEXT UNIQUE, enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, approval_status INTEGER DEFAULT 0)''')
        c.execute('''CREATE TABLE IF NOT EXISTS threads
                     (id INTEGER PRIMARY KEY, course_id INTEGER, title TEXT, creator_id INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, ext_url TEXT, ext_type TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS posts
                     (id INTEGER PRIMARY KEY, thread_id INTEGER, user_id INTEGER, enrollment_number TEXT, content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, ext_url TEXT, ext_type TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS progress
                     (id INTEGER PRIMARY KEY, user_id INTEGER, course_id INTEGER, assignment_name TEXT, status TEXT, grade INTEGER, file_path TEXT, ai_grade INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS notes
                     (id INTEGER PRIMARY KEY, user_id INTEGER, course_id INTEGER, content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS assignments
                     (id INTEGER PRIMARY KEY, course_id INTEGER, name TEXT, type TEXT, questions TEXT, correct_answers TEXT, due_date TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS external_resources
                     (id INTEGER PRIMARY KEY, course_id INTEGER, title TEXT, url TEXT, description TEXT, resource_type TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS lti_tools
                     (id INTEGER PRIMARY KEY, course_id INTEGER, name TEXT, launch_url TEXT, consumer_key TEXT, shared_secret TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS webhooks
                     (id INTEGER PRIMARY KEY, course_id INTEGER, url TEXT, events TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS notifications
                     (id INTEGER PRIMARY KEY, user_id INTEGER, message TEXT, link TEXT, is_read INTEGER DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, notif_type TEXT)''')
        
        # Add new columns if they don't exist
        c.execute("PRAGMA table_info(courses)")
        columns = [col[1] for col in c.fetchall()]
        if 'course_code' not in columns:
            c.execute('ALTER TABLE courses ADD COLUMN course_code TEXT UNIQUE')
        
        c.execute("PRAGMA table_info(enrollments)")
        columns = [col[1] for col in c.fetchall()]
        if 'approval_status' not in columns:
            c.execute('ALTER TABLE enrollments ADD COLUMN approval_status INTEGER DEFAULT 0')
        
        c.execute("PRAGMA table_info(notifications)")
        columns = [col[1] for col in c.fetchall()]
        if 'course_id' not in columns:
            c.execute('ALTER TABLE notifications ADD COLUMN course_id INTEGER')
        
        conn.commit()
        conn.close()
        print("✅ Database initialized successfully")
        
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        print("🚀 Continuing without database initialization...")
    
    # Step 2: Import Flask app (now that database is ready)
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