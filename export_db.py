#!/usr/bin/env python3
"""
Export database data for migration to Railway
"""

import sqlite3
import json
import os

def export_database():
    """Export all data from local database"""
    
    if not os.path.exists('database.db'):
        print("❌ Local database.db not found!")
        return
    
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        # Get all table names
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in c.fetchall()]
        
        data = {}
        
        for table in tables:
            print(f"📊 Exporting table: {table}")
            c.execute(f"SELECT * FROM {table}")
            rows = c.fetchall()
            
            # Get column names
            c.execute(f"PRAGMA table_info({table})")
            columns = [col[1] for col in c.fetchall()]
            
            # Convert to list of dictionaries
            table_data = []
            for row in rows:
                row_dict = dict(zip(columns, row))
                table_data.append(row_dict)
            
            data[table] = table_data
            print(f"✅ Exported {len(table_data)} rows from {table}")
        
        conn.close()
        
        # Save to JSON file
        with open('database_export.json', 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        print(f"✅ Database exported to database_export.json")
        print(f"📁 File size: {os.path.getsize('database_export.json')} bytes")
        
        # Show summary
        print("\n📋 Export Summary:")
        for table, rows in data.items():
            print(f"   {table}: {len(rows)} rows")
        
    except Exception as e:
        print(f"❌ Export failed: {e}")

if __name__ == '__main__':
    export_database() 