# Resume Parser Backend Setup Guide

## Environment Variables

The backend requires the following environment variables to be set:

### Required Variables

1. **GROQ_API_KEY**: Your Groq API key for AI-powered resume parsing
   - Get your API key from: https://console.groq.com/
   - Add to your environment: `GROQ_API_KEY=your_api_key_here`

### Local Development Setup

1. Create a `.env` file in the backend directory:
```bash
# Backend/.env
GROQ_API_KEY=your_groq_api_key_here
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run the backend locally:
```bash
python app.py
```

### Deployment Setup (Render/Heroku)

1. Set environment variables in your deployment platform:
   - `GROQ_API_KEY`: Your Groq API key

2. Deploy the backend:
   - The `Procfile` and `wsgi.py` are already configured for deployment

## Troubleshooting

### Common Issues

1. **"API key configuration error on server"**
   - Solution: Ensure `GROQ_API_KEY` is set in your environment variables
   - Check deployment platform settings

2. **"No text could be extracted from the uploaded resume"**
   - Solution: Ensure the resume file is not corrupted
   - Try with a different resume file
   - Check if the file format is supported (PDF or DOCX)

3. **"AI response format is invalid"**
   - Solution: This usually indicates an issue with the Groq API
   - Check your API key is valid
   - Verify you have sufficient API credits

4. **"Failed to parse resume data from AI response"**
   - Solution: The AI model returned invalid JSON
   - Try with a simpler resume format
   - Check the backend logs for detailed error messages

### Testing

Run the debug script to test the backend:
```bash
cd backend
python debug_resume_parsing.py
```

This will test:
- Backend connectivity
- Resume parsing with file upload
- Resume parsing with text input

### Logs

Check the backend logs for detailed error messages:
- Local: Console output
- Deployment: Platform-specific log viewer

## API Endpoints

- `POST /parse-resume`: Parse resume file (PDF/DOCX)
- `POST /test-parse`: Parse resume text (for testing)
- `GET /test`: Health check endpoint
- `POST /start-interview`: Start interview session
- `POST /continue-interview`: Continue interview session

## File Format Support

- **PDF**: Uses PyPDF2 for text extraction
- **DOCX**: Uses python-docx for text extraction
- **Maximum file size**: 10MB
- **Maximum text length**: 20,000 characters (truncated if longer)
