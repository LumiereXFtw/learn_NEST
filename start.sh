#!/bin/bash

# Initialize database
python -c "from app import init_db; init_db()"

# Start the application with Gunicorn
gunicorn --config gunicorn_config.py app:app 