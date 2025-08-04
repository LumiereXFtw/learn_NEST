#!/usr/bin/env python3
"""
Test script to verify database import
"""

import sqlite3
import json
import os

def test_database():
    """Test if database has data"""
    
    if not os.path.exists('database.db'):
        print("❌ database.db not found!")
        return
    
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        print("📊 Checking database content...")
        
        # Check users
        c.execute('SELECT COUNT(*) FROM users')
        user_count = c.fetchone()[0]
        print(f"👥 Users: {user_count}")
        
        if user_count > 0:
            c.execute('SELECT username, role, is_approved FROM users LIMIT 5')
            users = c.fetchall()
            for user in users:
                print(f"   - {user[0]} ({user[1]}) - Approved: {user[2]}")
        
        # Check courses
        c.execute('SELECT COUNT(*) FROM courses')
        course_count = c.fetchone()[0]
        print(f"📚 Courses: {course_count}")
        
        if course_count > 0:
            c.execute('SELECT title, creator_id FROM courses LIMIT 3')
            courses = c.fetchall()
            for course in courses:
                print(f"   - {course[0]} (Creator: {course[1]})")
        
        # Check enrollments
        c.execute('SELECT COUNT(*) FROM enrollments')
        enrollment_count = c.fetchone()[0]
        print(f"🎓 Enrollments: {enrollment_count}")
        
        # Check other tables
        tables = ['threads', 'posts', 'progress', 'notes', 'assignments', 'notifications']
        for table in tables:
            try:
                c.execute(f'SELECT COUNT(*) FROM {table}')
                count = c.fetchone()[0]
                print(f"📋 {table.capitalize()}: {count}")
            except:
                print(f"❌ {table.capitalize()}: Table not found")
        
        conn.close()
        
        if user_count > 3:  # More than just initial users
            print("✅ Database has imported data!")
        else:
            print("⚠️ Database only has initial users")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == '__main__':
    test_database() 