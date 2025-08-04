# LearnNest Enhanced

A comprehensive Learning Management System (LMS) built with Flask, featuring course management, student enrollment, assignments, forums, and real-time chat capabilities.

## 🚀 Features

### Core Features
- **Multi-role System**: Admin, Instructor, and Student roles with isolated permissions
- **Course Management**: Create, edit, and manage courses with unique course codes
- **Student Enrollment**: Course-specific registration with instructor approval workflow
- **Assignment System**: Create and submit assignments with AI-powered grading
- **Forum & Discussions**: Thread-based discussions with AI feedback
- **Real-time Chat**: Live chat functionality for course participants
- **Progress Tracking**: Monitor student progress and completion rates
- **File Management**: Upload and manage course resources and assignments
- **Notification System**: Real-time notifications for important events

### Performance Optimizations
- **Database Connection Pooling**: Optimized SQLite connections for better performance
- **Lazy Loading**: Heavy dependencies (NLTK, Gemini AI) load only when needed
- **Caching**: Flask-Caching implementation for faster response times
- **Static File Optimization**: 1-year cache headers for uploaded files
- **Production Configuration**: Separate configs for development and production

### Security Features
- **Role-based Access Control**: Granular permissions based on user roles
- **Payment Verification**: Screenshot proof of payment for student registration
- **API Token Management**: Secure API access for admin users only
- **Session Security**: Secure cookie configuration for production

## 🛠️ Technology Stack

- **Backend**: Flask 2.3.3
- **Database**: SQLite with WAL mode
- **Real-time**: Flask-SocketIO with Eventlet
- **AI Integration**: Google Gemini AI for feedback and grading
- **Authentication**: Flask-Login
- **Caching**: Flask-Caching
- **Production Server**: Gunicorn with Eventlet workers

## 📦 Installation

### Prerequisites
- Python 3.8+
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/LumiereXFtw/learnnest_enhanced.git
   cd learnnest_enhanced
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   ```bash
   cp env.example .env
   # Edit .env file with your configuration
   ```

4. **Initialize Database**
   ```bash
   python -c "from app import init_db; init_db()"
   ```

5. **Run the Application**
   ```bash
   # Development
   python app.py
   
   # Production
   ./start.sh
   ```

## 🔧 Configuration

### Environment Variables
Create a `.env` file with the following variables:

```env
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
FLASK_ENV=production
```

### Database Configuration
The application uses SQLite with the following optimizations:
- WAL mode for better concurrency
- Connection pooling for improved performance
- Proper indexing for faster queries

## 🚀 Deployment

### Render Deployment
1. Connect your GitHub repository to Render
2. Set environment variables in Render dashboard
3. Use the provided `start.sh` script as the build command
4. Configure the service to use port 10000

### Production Configuration
- Gunicorn with Eventlet workers
- Optimized for Render's infrastructure
- Automatic database initialization
- Static file caching

## 📊 Performance Features

### Database Optimizations
- Thread-local connection pooling
- WAL mode for better concurrency
- Optimized PRAGMA settings
- Connection reuse for better performance

### Caching Strategy
- Flask-Caching for frequently accessed data
- 1-year cache headers for static files
- Context processor caching for user logos

### Lazy Loading
- NLTK downloads only when needed
- Gemini AI initialization on-demand
- Heavy imports deferred until required

## 🔐 Security

### Authentication & Authorization
- Flask-Login for session management
- Role-based access control
- Secure cookie configuration
- API token management for admin users

### Data Protection
- Password hashing with Werkzeug
- Secure file upload handling
- Input validation and sanitization
- CSRF protection

## 📈 Monitoring & Analytics

### Built-in Analytics
- Course enrollment statistics
- Student progress tracking
- Assignment completion rates
- User activity monitoring

### Error Handling
- Comprehensive error pages
- Logging for debugging
- Graceful error recovery

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the code comments

## 🔄 Changelog

### Version 1.0.0 (Current)
- Initial release with performance optimizations
- Complete LMS functionality
- Production-ready deployment configuration
- Enhanced security features
- Real-time communication capabilities

---

**LearnNest Enhanced** - Empowering education through technology