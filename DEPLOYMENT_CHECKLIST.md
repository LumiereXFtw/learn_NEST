# 🚀 Railway Deployment Checklist

## ✅ Pre-Deployment Checklist

- [ ] **Code is on GitHub** - Repository is public or Railway has access
- [ ] **Gemini API Key** - Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- [ ] **Railway Account** - Sign up at [railway.app](https://railway.app)
- [ ] **Test Locally** - App runs without errors on your machine

## 🎯 Railway Deployment Steps

### Step 1: Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/learnnest_enhanced.git
git push -u origin main
```

### Step 2: Deploy on Railway
1. Go to [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository

### Step 3: Configure Environment Variables
Add these in Railway dashboard:
```env
SECRET_KEY=your-super-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
FLASK_ENV=production
```

### Step 4: Wait for Deployment
- Railway will automatically detect Python app
- Uses `railway_start.py` for startup
- Takes 2-3 minutes to deploy

## ✅ Post-Deployment Verification

- [ ] **App loads** - No errors on homepage
- [ ] **Login works** - Can register and login
- [ ] **File uploads** - Uploads persist after refresh
- [ ] **Database works** - Data is saved
- [ ] **Real-time chat** - WebSocket connections work
- [ ] **All features** - Course creation, assignments, etc.

## 🔧 Troubleshooting

### If App Won't Start:
- Check Railway logs
- Verify environment variables
- Ensure all files are committed

### If Features Don't Work:
- Check browser console for errors
- Verify database initialization
- Test file permissions

## 📞 Quick Support

- **Railway Logs** - Check deployment tab
- **Environment Variables** - Verify in settings
- **GitHub Repository** - Ensure code is pushed

---

**🎯 Your LearnNest Enhanced will be live and fast on Railway!** 