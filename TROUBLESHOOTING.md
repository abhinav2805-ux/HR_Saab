# Resume Parser Troubleshooting Guide

## Quick Diagnosis

### Step 1: Test Backend Connection
1. Go to the Resume Upload page
2. Click the "🔍 Test Backend Connection" button
3. Check if you get a success message

### Step 2: Check Environment Variables
The most common issue is missing API keys. Ensure you have:
- `GROQ_API_KEY` set in your backend environment

## Common Issues and Solutions

### 1. "API key configuration error on server"
**Problem**: The Groq API key is not configured
**Solution**: 
- Get a Groq API key from https://console.groq.com/
- Set it in your deployment environment variables
- For local development, create a `.env` file in the backend directory

### 2. "No resume file provided"
**Problem**: File upload is not working
**Solution**:
- Ensure you're selecting a file before clicking "Parse Resume"
- Check that the file is in PDF or DOCX format
- Try with a different browser

### 3. "No text could be extracted from the uploaded resume"
**Problem**: The resume file cannot be read
**Solutions**:
- Try with a different resume file
- Ensure the file is not password-protected
- Check if the file is corrupted
- Try converting the file to a different format

### 4. "AI response format is invalid"
**Problem**: The AI model returned unexpected data
**Solutions**:
- Check your Groq API key is valid
- Ensure you have sufficient API credits
- Try with a simpler resume format
- Check the backend logs for detailed errors

### 5. "Failed to parse resume data from AI response"
**Problem**: The AI returned invalid JSON
**Solutions**:
- The backend will automatically retry with cleaned data
- Try with a different resume file
- Check if the resume has unusual formatting

### 6. Frontend shows "No response from server"
**Problem**: Backend is not accessible
**Solutions**:
- Check if the backend is deployed and running
- Verify the API URL in the frontend configuration
- Check for CORS issues

## Testing Your Setup

### Run the Debug Script
```bash
cd backend
python debug_resume_parsing.py
```

This will test:
- ✅ Backend connectivity
- ✅ Resume parsing with file upload
- ✅ Resume parsing with text input

### Manual Testing
1. **Test Backend Health**:
   ```bash
   curl https://hr-saab.onrender.com/test
   ```

2. **Test Resume Parsing**:
   ```bash
   curl -X POST https://hr-saab.onrender.com/test-parse \
     -H "Content-Type: application/json" \
     -d '{"resume_text": "John Doe\nSoftware Engineer"}'
   ```

## Environment Setup

### Local Development
1. Create `.env` file in backend directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run backend:
   ```bash
   python app.py
   ```

### Deployment (Render/Heroku)
1. Set environment variables in your deployment platform:
   - `GROQ_API_KEY`: Your Groq API key

2. Deploy using the existing configuration

## File Format Support

| Format | Support | Notes |
|--------|---------|-------|
| PDF    | ✅      | Uses PyPDF2 |
| DOCX   | ✅      | Uses python-docx |
| DOC    | ❌      | Not supported |
| TXT    | ❌      | Not supported |

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/test` | GET | Health check |
| `/parse-resume` | POST | Parse resume file |
| `/test-parse` | POST | Parse resume text (testing) |
| `/start-interview` | POST | Start interview |
| `/continue-interview` | POST | Continue interview |

## Logs and Debugging

### Backend Logs
- **Local**: Check console output
- **Deployment**: Use platform-specific log viewer
- **Key log levels**: DEBUG, INFO, ERROR

### Frontend Debugging
- Open browser developer tools
- Check Network tab for API calls
- Check Console tab for JavaScript errors

## Performance Tips

1. **File Size**: Keep resume files under 10MB
2. **Text Length**: Backend truncates to 20,000 characters
3. **API Limits**: Groq has rate limits, avoid rapid requests
4. **Caching**: Consider caching parsed results

## Getting Help

If you're still having issues:

1. **Check the logs**: Look for specific error messages
2. **Test with debug script**: Run `debug_resume_parsing.py`
3. **Verify API key**: Ensure Groq API key is valid
4. **Try different file**: Test with a simple resume
5. **Check deployment**: Ensure backend is running

## Common Error Messages

| Error Message | Likely Cause | Solution |
|---------------|--------------|----------|
| "API key configuration error" | Missing GROQ_API_KEY | Set environment variable |
| "No resume file provided" | File not selected | Select a file before upload |
| "Unsupported file type" | Wrong format | Use PDF or DOCX |
| "No text extracted" | File corrupted/encrypted | Try different file |
| "AI response format invalid" | API issue | Check API key and credits |
| "JSON decode error" | AI returned bad data | Try simpler resume |
| "No response from server" | Backend down | Check deployment status |
