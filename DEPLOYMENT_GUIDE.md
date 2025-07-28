# Deployment Guide for Resume Parser & AI Interview Simulator

## Backend Deployment (Render)

### 1. Environment Variables
Make sure these environment variables are set in your Render dashboard:
- `GROQ_API_KEY`: Your Groq API key for AI functionality

### 2. Build Command
```bash
pip install -r requirements.txt
```

### 3. Start Command
```bash
gunicorn app:app
```

### 4. Health Check
Your backend should be accessible at: `https://hr-saab.onrender.com/health`

## Frontend Deployment (Vercel)

### 1. Environment Variables
Set these in your Vercel dashboard (Settings → Environment Variables):

**Production Environment:**
- `VITE_API_BASE_URL`: `https://hr-saab.onrender.com`

**Preview Environment:**
- `VITE_API_BASE_URL`: `https://hr-saab.onrender.com`

### 2. Build Settings
- **Framework Preset**: Vite
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`

### 3. Domain
Your frontend will be accessible at: `https://resume-p.vercel.app`

## Testing the Deployment

### 1. Test Backend Connection
1. Go to your deployed frontend
2. Click the "Test Backend Connection" button
3. Check the console for any errors
4. You should see a success message if the connection works

### 2. Test Resume Upload
1. Upload a PDF or DOCX resume
2. Check if the parsing works correctly
3. Verify the parsed data is displayed

### 3. Test Interview Flow
1. Start an interview after resume upload
2. Check if the interview questions are generated
3. Test the conversation flow

## Common Issues & Solutions

### 1. CORS Errors
- **Issue**: Frontend can't connect to backend
- **Solution**: Backend CORS is configured for `https://resume-p.vercel.app` (without trailing slash)

### 2. Environment Variable Issues
- **Issue**: Frontend still uses localhost
- **Solution**: Ensure `VITE_API_BASE_URL` is set correctly in Vercel

### 3. API Key Issues
- **Issue**: Backend returns API key errors
- **Solution**: Verify `GROQ_API_KEY` is set in Render environment variables

### 4. File Upload Issues
- **Issue**: Resume upload fails
- **Solution**: Check file size (max 10MB) and format (PDF/DOCX only)

## Debugging

### 1. Check Backend Logs
- Go to your Render dashboard
- Check the logs for any errors

### 2. Check Frontend Console
- Open browser developer tools
- Check the console for any JavaScript errors

### 3. Test API Endpoints
- Test `/health` endpoint: `https://hr-saab.onrender.com/health`
- Test `/test` endpoint: `https://hr-saab.onrender.com/test`

## File Structure
```
resumeparser/
├── backend/
│   ├── app.py (main Flask application)
│   ├── requirements.txt (Python dependencies)
│   └── Procfile (Render deployment config)
└── frontend/
    ├── src/
    │   ├── services/api.ts (API service)
    │   ├── pages/ResumeUploadPage.tsx (main upload page)
    │   └── pages/InterviewPage.tsx (interview interface)
    ├── package.json (Node.js dependencies)
    └── vite.config.ts (Vite configuration)
```

## Support
If you encounter issues:
1. Check the browser console for errors
2. Verify all environment variables are set
3. Test the backend endpoints directly
4. Check the deployment logs in Render/Vercel 