#!/usr/bin/env python3
"""
Copy database file directly to Railway
"""

import shutil
import os

def copy_database():
    """Copy the database file to Railway"""
    
    source_db = 'database.db'
    railway_db = 'database_railway.db'
    
    if not os.path.exists(source_db):
        print(f"❌ {source_db} not found!")
        return False
    
    try:
        # Copy the database file
        shutil.copy2(source_db, railway_db)
        print(f"✅ Database copied: {source_db} -> {railway_db}")
        print(f"📁 File size: {os.path.getsize(railway_db)} bytes")
        return True
    except Exception as e:
        print(f"❌ Failed to copy database: {e}")
        return False

if __name__ == '__main__':
    copy_database() 