# Resume Parser Debugging Guide

This guide will help you troubleshoot issues with the resume parsing functionality.

## 🚀 Quick Start

1. **Test Backend Connection**: Click the "Test Backend Connection" button in the frontend
2. **Check Browser Console**: Open Developer Tools (F12) and check the Console tab
3. **Run Test Script**: Use the provided test script to debug backend issues

## 🔍 Common Issues and Solutions

### 1. "Failed to parse resume data" Error

**Cause**: The AI model returned malformed JSON or unexpected response format.

**Solutions**:
- ✅ **Fixed**: Improved prompt with strict JSON schema
- ✅ **Fixed**: Added better error logging to see the exact AI response
- ✅ **Fixed**: Enhanced JSON cleaning and validation

**Debug Steps**:
1. Check the backend logs for the exact AI response
2. Look for the "JSON decoding error for content" log message
3. Verify the AI response follows the expected schema

### 2. "No text could be extracted from the PDF" Error

**Cause**: PDF is scanned/image-based or corrupted.

**Solutions**:
- Try uploading a .docx file instead
- Ensure the PDF contains selectable text (not just images)
- Use a text-based PDF for testing

### 3. Backend Connection Issues

**Cause**: Server is down, CORS issues, or network problems.

**Debug Steps**:
1. Click "Test Backend Connection" button
2. Check if the backend URL is correct
3. Verify the server is running and accessible

### 4. Skills Display Issues

**Cause**: Data structure mismatch between frontend and backend.

**Solutions**:
- ✅ **Fixed**: Updated frontend to handle the new skills structure `{ skills: [...] }`
- ✅ **Fixed**: Added fallback displays for missing data

## 🛠️ Debugging Tools

### 1. Frontend Debugging

**Browser Developer Tools**:
```javascript
// Check API responses in Network tab
// Look for /parse-resume requests
// Check response status and content
```

**Console Logging**:
- The frontend now logs API response keys and data
- Check for "API Response keys:" and "API Response data:" messages

### 2. Backend Debugging

**Test Script**:
```bash
cd backend
python test_resume_parsing.py
```

**Manual API Testing**:
```bash
# Test backend connection
curl https://hr-saab.onrender.com/test

# Test resume parsing (replace with your file)
curl -X POST -F "resume=@your_resume.pdf" https://hr-saab.onrender.com/parse-resume
```

### 3. Environment Variables

**Check .env file**:
```bash
# Ensure these are set in your .env file
GROQ_API_KEY=your_groq_api_key_here
```

## 📊 Expected Data Structure

After the fixes, the API should return:

```json
{
  "name": "John Doe",
  "skills": {
    "skills": ["JavaScript", "Python", "React", "Node.js"]
  },
  "experience": [
    {
      "title": "Software Engineer",
      "company": "TechCorp",
      "duration": "2022-Present",
      "description": "Led development of web applications",
      "achievements": ["Achievement 1", "Achievement 2"]
    }
  ],
  "projects": [
    {
      "title": "E-commerce Platform",
      "description": "Full-stack application",
      "link": "https://github.com/project"
    }
  ]
}
```

## 🔧 Troubleshooting Steps

### Step 1: Test Basic Connectivity
1. Open browser Developer Tools (F12)
2. Click "Test Backend Connection" button
3. Check Console for any errors
4. Verify the response shows "Backend connection successful"

### Step 2: Test Resume Upload
1. Prepare a simple text-based PDF or DOCX file
2. Upload the file through the frontend
3. Check Console for API response logs
4. Look for "API Response keys:" and "API Response data:" messages

### Step 3: Check Backend Logs
1. If using the test script, check the output
2. Look for any error messages or malformed JSON
3. Verify the AI response format

### Step 4: Validate Data Structure
1. Ensure the parsed data has the expected structure
2. Check that skills, experience, and projects are properly formatted
3. Verify the frontend displays the data correctly

## 🐛 Common Error Messages

| Error Message | Cause | Solution |
|---------------|-------|----------|
| "Failed to parse resume data" | Malformed AI response | Check backend logs for exact response |
| "No text could be extracted" | PDF format issues | Try DOCX file or text-based PDF |
| "Backend connection failed" | Server/network issues | Check server status and URL |
| "Missing expected fields" | Data structure mismatch | Verify API response format |

## 📝 Testing Checklist

- [ ] Backend connection test passes
- [ ] Environment variables are set correctly
- [ ] Test with a simple text-based PDF
- [ ] Test with a DOCX file
- [ ] Check browser console for errors
- [ ] Verify parsed data structure
- [ ] Confirm frontend displays data correctly
- [ ] Test interview flow after parsing

## 🆘 Getting Help

If you're still experiencing issues:

1. **Check the logs**: Look for specific error messages
2. **Test with sample data**: Use the provided test script
3. **Verify file format**: Ensure you're using supported file types
4. **Check API limits**: Verify your Groq API key has sufficient credits

## 📈 Performance Tips

- Use text-based PDFs for better extraction
- Keep resume files under 10MB
- Ensure resumes have clear, structured content
- Test with simple resumes first before complex ones 