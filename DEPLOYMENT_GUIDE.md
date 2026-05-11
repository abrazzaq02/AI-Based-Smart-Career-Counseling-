# 🚀 Deployment Guide — Smart Career Counseling System

## Overview
This guide will walk you through deploying the Smart Career Counseling System to **Streamlit Community Cloud** for free hosting.

---

## Prerequisites
Before you begin, make sure you have:
- ✅ Git installed and configured (Already done ✓)
- ✅ GitHub account (Free - https://github.com/signup)
- ✅ Streamlit account (Free - https://streamlit.io/cloud)

---

## Step 1: Create a GitHub Repository

### Option A: Using GitHub Web Interface (Recommended)

1. Go to https://github.com/new
2. Fill in the repository details:
   - **Repository name**: `career-counseling-system` (or your preferred name)
   - **Description**: `AI-Based Smart Career Counseling Expert System using KRR`
   - **Public**: ✓ (Public repository is required for free Streamlit Cloud)
   - **Initialize repository**: Leave unchecked (we already have code)
3. Click **Create repository**

### Option B: Using GitHub CLI

```bash
gh repo create career-counseling-system --public --source=. --remote=origin --push
```

---

## Step 2: Connect Local Repository to GitHub

### Step 2a: Copy your repository URL

1. On your GitHub repository page, click the **Code** button
2. Copy the HTTPS URL (example: `https://github.com/yourusername/career-counseling-system.git`)

### Step 2b: Add remote and push code

```bash
cd c:\Users\sys\Downloads\career_gui

# Add the remote repository
git remote add origin https://github.com/yourusername/career-counseling-system.git

# Rename branch to main (GitHub default)
git branch -M main

# Push code to GitHub
git push -u origin main
```

**Note**: Replace `yourusername` with your actual GitHub username.

---

## Step 3: Deploy on Streamlit Community Cloud

### Step 3a: Sign up for Streamlit Cloud

1. Go to https://streamlit.io/cloud
2. Click **Sign in with GitHub**
3. Authorize Streamlit to access your GitHub repositories
4. Create your Streamlit account

### Step 3b: Deploy the Application

1. After signing in, click **Create app**
2. Fill in the deployment details:
   - **Repository**: Select your repository (e.g., `yourusername/career-counseling-system`)
   - **Branch**: Select `main`
   - **Main file path**: `app.py`
3. Click **Deploy!**

Streamlit will automatically:
- Install dependencies from `requirements.txt`
- Build the Docker container
- Deploy your app to a live URL

---

## Step 4: Access Your Deployed App

Your app will be available at:
```
https://career-counseling-system.streamlit.app
```

(URL format: `https://<your-app-name>.streamlit.app`)

---

## Configuration Files Already Prepared

### ✅ `.gitignore`
Excludes unnecessary files from Git tracking

### ✅ `.streamlit/config.toml`
Streamlit configuration with custom theme colors:
- Primary Color: `#6C63FF` (Purple)
- Background: `#0a0e1a` (Dark)
- Theme: Custom dark mode

### ✅ `requirements.txt`
All Python dependencies for the application

---

## Troubleshooting Deployment

### Issue: "Repository not found" error
**Solution**: 
- Check that your repository URL is correct
- Ensure you're using HTTPS (not SSH)
- Verify you're in the correct directory

### Issue: Module import errors on Streamlit Cloud
**Solution**: 
- Ensure all imports are in `requirements.txt`
- Check for typos in filenames (case-sensitive on Linux)
- Verify the main file is `app.py`

### Issue: App crashes after deployment
**Solution**: 
- Check the Streamlit Cloud logs (Dashboard → App → Logs)
- Look for missing dependencies
- Ensure all relative paths use `/` (not `\`)

### Issue: Slow deployment or timeout
**Solution**: 
- This is normal for first deployment (can take 2-5 minutes)
- Streamlit Cloud is building a Docker container
- Subsequent deployments are faster

---

## Making Updates After Deployment

Once deployed, any changes you push to GitHub will automatically trigger a redeploy:

```bash
# Make changes to your code
nano app.py

# Stage and commit changes
git add .
git commit -m "Update: Your change description"

# Push to GitHub
git push origin main
```

Streamlit will automatically detect the push and redeploy your app (takes ~1-2 minutes).

---

## Environment Variables (Optional)

If you need to add secrets or API keys:

1. In Streamlit Cloud Dashboard, go to your app
2. Click **Settings** → **Secrets**
3. Add your secrets in TOML format:
   ```
   db_password = "your_password"
   api_key = "your_key"
   ```
4. Access in your code:
   ```python
   import streamlit as st
   password = st.secrets["db_password"]
   ```

---

## Monitoring Your Deployed App

### View App Logs
1. Go to https://share.streamlit.io
2. Select your app
3. Click **Logs** to see real-time activity

### Restart App
1. Click **Settings** → **Reboot app**
2. App will restart and process cached data

### Delete App
1. Click **Settings** → **Delete app**
2. Confirm deletion

---

## Performance Tips

1. **Caching**: Use `@st.cache_data` for expensive operations
   ```python
   @st.cache_data
   def load_data():
       return expensive_operation()
   ```

2. **Session State**: Use `st.session_state` to avoid recalculating
   ```python
   if 'results' not in st.session_state:
       st.session_state.results = run_inference()
   ```

3. **Lazy Loading**: Load heavy libraries only when needed

---

## Domain Configuration (Optional)

To use a custom domain:

1. In Streamlit Cloud Dashboard → App Settings
2. Under "Custom domain", enter your domain
3. Update DNS records with CNAME to `share.streamlit.io`

---

## Git Commands Cheat Sheet

```bash
# Check status
git status

# View commit history
git log --oneline

# View remote
git remote -v

# Create new branch for features
git checkout -b feature/my-feature

# Switch branch
git checkout main

# Pull latest changes
git pull origin main

# Push changes
git push origin main
```

---

## Frequently Asked Questions

**Q: Is Streamlit Cloud free?**
A: Yes! Free tier includes 1 app, 3 secrets, and shared CPU resources.

**Q: Can I use a private repository?**
A: Yes, but you need to authorize Streamlit to access private repos.

**Q: How often are apps updated?**
A: Apps update automatically when you push to GitHub (within 2 minutes).

**Q: What's the storage limit?**
A: 1GB per app on free tier.

**Q: Can I use a database?**
A: Yes! You can connect to any cloud database (Firebase, PostgreSQL, MongoDB, etc.)

---

## Next Steps After Deployment

1. **Test your app**: Visit the live URL and test all features
2. **Share with others**: Send the app link to users
3. **Monitor performance**: Check logs regularly
4. **Gather feedback**: Ask users for feedback
5. **Iterate**: Make improvements and push updates

---

## Support & Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Community Cloud**: https://streamlit.io/cloud
- **GitHub Docs**: https://docs.github.com
- **Stack Overflow**: Tag your questions with `streamlit`

---

## Current Project Status

```
✅ Local Git Repository: Initialized
✅ All Files: Committed
✅ Config Files: Created
✅ Requirements: Ready
✅ Code: Production-ready

Next Step: Push to GitHub
```

---

## Quick Start Command

Once you have your GitHub URL, run:

```bash
cd c:\Users\sys\Downloads\career_gui

git remote add origin https://github.com/yourusername/career-counseling-system.git
git branch -M main
git push -u origin main
```

Then deploy on https://streamlit.io/cloud

---

**Generated**: May 12, 2026
**Project**: Smart Career Counseling Expert System
**Status**: Ready for Cloud Deployment
