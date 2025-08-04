#!/bin/bash

# Railway build script for LearnNest Enhanced
echo "🚀 Building LearnNest Enhanced..."

# Install Python dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories (these will be empty on Railway)
echo "📁 Creating directories..."
mkdir -p uploads
mkdir -p assignment_uploads
mkdir -p static/uploads

# Create placeholder files to ensure directories exist
touch uploads/.gitkeep
touch assignment_uploads/.gitkeep
touch static/uploads/.gitkeep

echo "✅ Build completed successfully!" 