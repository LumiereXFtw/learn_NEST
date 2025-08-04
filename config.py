import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    UPLOAD_FOLDER = 'Uploads'
    ASSIGNMENT_UPLOAD_FOLDER = 'assignment_uploads'
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
    ALLOWED_SUBTITLE_EXTENSIONS = {'vtt', 'srt'}
    
    # Database settings
    DATABASE_PATH = 'database.db'
    
    # Cache settings
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300  # 5 minutes
    
    # Session settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = True
    
    # Security settings
    WTF_CSRF_CHECK_DEFAULT = False
    
    # Performance settings
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year cache for static files
    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    
    # Production database settings
    DATABASE_PATH = os.getenv('DATABASE_URL', 'database.db')
    
    # Production cache settings
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 600  # 10 minutes
    
    # Production session settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = True
    
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    
    # Development cache settings
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60  # 1 minute
    
    # Development session settings
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = False

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 