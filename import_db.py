#!/usr/bin/env python3
"""
Import database data on Railway
"""

import sqlite3
import json
import os

def import_database():
    """Import data from JSON file to database"""
    
    if not os.path.exists('database_export.json'):
        print("❌ database_export.json not found!")
        return
    
    try:
        # Load data from JSON
        with open('database_export.json', 'r') as f:
            data = json.load(f)
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        print("📊 Importing database data...")
        
        for table, rows in data.items():
            if not rows:
                continue
                
            print(f"📥 Importing {len(rows)} rows to {table}")
            
            for row in rows:
                # Remove id if it exists (let SQLite auto-generate)
                if 'id' in row:
                    del row['id']
                
                # Build INSERT statement
                columns = list(row.keys())
                placeholders = ', '.join(['?' for _ in columns])
                column_names = ', '.join(columns)
                
                query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
                values = list(row.values())
                
                try:
                    c.execute(query, values)
                except Exception as e:
                    print(f"⚠️ Skipping row in {table}: {e}")
                    continue
        
        conn.commit()
        conn.close()
        
        print("✅ Database import completed successfully!")
        
    except Exception as e:
        print(f"❌ Import failed: {e}")

if __name__ == '__main__':
    import_database() 