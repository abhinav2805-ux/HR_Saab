# AI Interview Simulator

A modern web application that uses AI to parse resumes and conduct virtual interviews. Built with React, TypeScript, and Flask.

## Features

- **Resume Parsing**: Upload PDF or DOCX resumes and extract structured data
- **AI-Powered Interviews**: Conduct realistic interviews based on resume content
- **Modern UI**: Beautiful, responsive interface with Tailwind CSS
- **Real-time Feedback**: Get instant feedback and scoring during interviews

## Tech Stack

### Frontend
- React 18 with TypeScript
- Tailwind CSS for styling
- Vite for build tooling
- React Router for navigation

### Backend
- Flask (Python)
- Groq AI for resume parsing and interview questions
- CORS enabled for cross-origin requests
- File upload support (PDF/DOCX)

## Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Groq API key

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

4. Run the backend:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser to `http://localhost:5173`

## Usage

1. **Upload Resume**: Drag and drop or select a PDF/DOCX resume file
2. **Parse Data**: The AI will extract name, skills, experience, and projects
3. **Start Interview**: Click "Launch Virtual Interview" to begin
4. **Answer Questions**: Respond to AI-generated questions based on your resume
5. **Get Feedback**: Receive real-time feedback and scoring

## API Endpoints

- `POST /parse-resume`: Parse uploaded resume file
- `POST /start-interview`: Start a new interview session
- `POST /continue-interview`: Continue interview with user response
- `GET /health`: Health check endpoint

## Deployment

### Backend (Render/Heroku)
1. Set environment variable: `GROQ_API_KEY`
2. Deploy using the provided `Procfile` and `wsgi.py`

### Frontend (Vercel/Netlify)
1. Build the project: `npm run build`
2. Deploy the `dist` folder

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key for AI functionality

## File Support

- **PDF**: Uses PyPDF2 for text extraction
- **DOCX**: Uses python-docx for text extraction
- **Maximum file size**: 10MB
- **Maximum text length**: 20,000 characters

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details
