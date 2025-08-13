#!/usr/bin/env python3
"""
Debug script for resume parsing issues
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BACKEND_URL = "https://hr-saab.onrender.com"

def test_backend_health():
    """Test if backend is accessible"""
    print("🔍 Testing backend health...")
    try:
        response = requests.get(f"{BACKEND_URL}/test", timeout=10)
        print(f"✅ Backend health check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend response: {data}")
            print(f"✅ Groq API key configured: {data.get('groq_api_key_set', False)}")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend health check failed: {e}")
        return False

def test_resume_parsing_with_file():
    """Test resume parsing with a sample file"""
    print("\n📄 Testing resume parsing with file upload...")
    
    # Create a simple test resume content
    test_resume_content = """
John Doe
Software Engineer
john.doe@email.com | (555) 123-4567

SUMMARY
Experienced software engineer with 5+ years developing web applications.

SKILLS
JavaScript, Python, React, Node.js, SQL, Git, Docker

EXPERIENCE
Senior Software Engineer | TechCorp | 2022-Present
• Led development of microservices architecture
• Implemented CI/CD pipeline reducing deployment time by 60%
• Mentored junior developers

Software Engineer | StartupXYZ | 2020-2022
• Built RESTful APIs using Node.js and Express
• Developed React frontend with TypeScript

PROJECTS
E-commerce Platform | github.com/johndoe/ecommerce
• Full-stack application with React and Node.js
• Integrated payment processing with Stripe API
"""
    
    try:
        # Create a mock file
        files = {
            'resume': ('test_resume.docx', test_resume_content.encode('utf-8'), 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }
        
        print("📤 Sending resume file to backend...")
        response = requests.post(
            f"{BACKEND_URL}/parse-resume",
            files=files,
            timeout=60  # Increased timeout for AI processing
        )
        
        print(f"📥 Response status: {response.status_code}")
        print(f"📥 Response headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ Resume parsing successful!")
                print(f"✅ Parsed data keys: {list(data.keys())}")
                print(f"✅ Name: {data.get('name', 'Not found')}")
                print(f"✅ Skills count: {len(data.get('skills', {}).get('skills', []))}")
                print(f"✅ Experience count: {len(data.get('experience', []))}")
                print(f"✅ Projects count: {len(data.get('projects', []))}")
                
                # Pretty print the full response
                print("\n📋 Full parsed data:")
                print(json.dumps(data, indent=2))
                return True
            except json.JSONDecodeError as e:
                print(f"❌ JSON decode error: {e}")
                print(f"❌ Raw response: {response.text}")
                return False
        else:
            print(f"❌ Resume parsing failed: {response.status_code}")
            print(f"❌ Error response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_resume_parsing_with_text():
    """Test resume parsing with text input using test-parse endpoint"""
    print("\n📝 Testing resume parsing with text input...")
    
    test_resume_text = """
John Doe
Software Engineer
john.doe@email.com

SKILLS
JavaScript, Python, React, Node.js, SQL

EXPERIENCE
Software Engineer | TechCorp | 2022-Present
• Built web applications using React and Node.js

PROJECTS
E-commerce Platform | github.com/johndoe/ecommerce
• Full-stack application with React and Node.js
"""
    
    try:
        response = requests.post(
            f"{BACKEND_URL}/test-parse",
            json={"resume_text": test_resume_text},
            timeout=60
        )
        
        print(f"📥 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Text parsing successful!")
            print(f"✅ Success: {data.get('success', False)}")
            if data.get('success') and data.get('data'):
                parsed_data = data['data']
                print(f"✅ Name: {parsed_data.get('name', 'Not found')}")
                print(f"✅ Skills count: {len(parsed_data.get('skills', {}).get('skills', []))}")
                print(f"✅ Experience count: {len(parsed_data.get('experience', []))}")
                print(f"✅ Projects count: {len(parsed_data.get('projects', []))}")
            return True
        else:
            print(f"❌ Text parsing failed: {response.status_code}")
            print(f"❌ Error response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🚀 Starting resume parsing debug tests...\n")
    
    # Test 1: Backend health
    if not test_backend_health():
        print("\n❌ Backend is not accessible. Please check the deployment.")
        return
    
    # Test 2: Resume parsing with file upload
    print("\n" + "="*50)
    file_success = test_resume_parsing_with_file()
    
    # Test 3: Resume parsing with text input
    print("\n" + "="*50)
    text_success = test_resume_parsing_with_text()
    
    # Summary
    print("\n" + "="*50)
    print("📊 Test Summary:")
    print(f"✅ Backend Health: {'PASS' if True else 'FAIL'}")
    print(f"✅ File Upload Parsing: {'PASS' if file_success else 'FAIL'}")
    print(f"✅ Text Input Parsing: {'PASS' if text_success else 'FAIL'}")
    
    if file_success and text_success:
        print("\n🎉 All tests passed! Resume parsing is working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the error messages above.")
        print("\n🔧 Troubleshooting tips:")
        print("1. Check if GROQ_API_KEY is set in environment variables")
        print("2. Verify the backend deployment is running")
        print("3. Check the backend logs for detailed error messages")
        print("4. Ensure the AI model is accessible and responding")

if __name__ == "__main__":
    main()
