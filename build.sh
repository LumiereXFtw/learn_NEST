#!/bin/bash

# Railway build script for LearnNest Enhanced
echo "🚀 Building LearnNest Enhanced..."

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads
mkdir -p assignment_uploads
mkdir -p static/uploads

echo "✅ Build completed successfully!" 