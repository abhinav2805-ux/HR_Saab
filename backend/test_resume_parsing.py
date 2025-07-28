#!/usr/bin/env python3
"""
Test script for resume parsing functionality
This script helps debug issues with the resume parsing API
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BACKEND_URL = "https://hr-saab.onrender.com"  # Update this to your backend URL
TEST_RESUME_TEXT = """
John Doe
Software Engineer
john.doe@email.com | (555) 123-4567 | linkedin.com/in/johndoe

SUMMARY
Experienced software engineer with 5+ years developing web applications using React, Node.js, and Python. Passionate about clean code and user experience.

SKILLS
Programming Languages: JavaScript, Python, Java, SQL
Frameworks: React, Node.js, Express, Django, Flask
Tools: Git, Docker, AWS, Jenkins
Databases: PostgreSQL, MongoDB, Redis

EXPERIENCE
Senior Software Engineer | TechCorp | 2022-Present
• Led development of microservices architecture serving 1M+ users
• Implemented CI/CD pipeline reducing deployment time by 60%
• Mentored 3 junior developers and conducted code reviews

Software Engineer | StartupXYZ | 2020-2022
• Built RESTful APIs using Node.js and Express
• Developed React frontend with TypeScript and Redux
• Collaborated with design team to implement responsive UI

PROJECTS
E-commerce Platform | github.com/johndoe/ecommerce
• Full-stack application with React frontend and Node.js backend
• Integrated payment processing with Stripe API
• Deployed on AWS with Docker containers

Task Management App | github.com/johndoe/taskmanager
• Real-time collaborative task management tool
• Built with React, Socket.io, and MongoDB
• Features drag-and-drop interface and real-time updates
"""

def test_backend_connection():
    """Test basic backend connectivity"""
    print("🔍 Testing backend connection...")
    try:
        response = requests.get(f"{BACKEND_URL}/test", timeout=10)
        print(f"✅ Backend connection successful: {response.status_code}")
        print(f"Response: {response.text}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend connection failed: {e}")
        return False

def test_resume_parsing():
    """Test resume parsing with sample data"""
    print("\n📄 Testing resume parsing...")
    
    # Create a mock file-like object
    class MockFile:
        def __init__(self, content):
            self.content = content
            self.filename = "test_resume.txt"
        
        def read(self):
            return self.content.encode('utf-8')
    
    mock_file = MockFile(TEST_RESUME_TEXT)
    
    try:
        # Test the parse-resume endpoint
        files = {'resume': ('test_resume.txt', mock_file.read(), 'text/plain')}
        response = requests.post(f"{BACKEND_URL}/parse-resume", files=files, timeout=30)
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Resume parsing successful!")
            print(f"Parsed data keys: {list(data.keys())}")
            print(f"Name: {data.get('name', 'Not found')}")
            print(f"Skills count: {len(data.get('skills', {}).get('skills', []))}")
            print(f"Experience count: {len(data.get('experience', []))}")
            print(f"Projects count: {len(data.get('projects', []))}")
            
            # Pretty print the full response
            print("\n📋 Full parsed data:")
            print(json.dumps(data, indent=2))
            
        else:
            print(f"❌ Resume parsing failed: {response.status_code}")
            print(f"Error response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        print(f"Raw response: {response.text}")

def test_environment():
    """Test environment configuration"""
    print("\n🔧 Testing environment configuration...")
    
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        print(f"✅ GROQ_API_KEY found: {groq_key[:10]}...")
    else:
        print("❌ GROQ_API_KEY not found in environment variables")
    
    print(f"Backend URL: {BACKEND_URL}")

def main():
    """Run all tests"""
    print("🚀 Starting resume parsing tests...\n")
    
    test_environment()
    if test_backend_connection():
        test_resume_parsing()
    
    print("\n✨ Tests completed!")

if __name__ == "__main__":
    main() 