#!/usr/bin/env python3
"""
Quick test to verify the resume parsing fix works
"""

import requests
import json

# Test the backend directly
BACKEND_URL = "https://hr-saab.onrender.com"

def test_backend_connection():
    """Test if backend is accessible"""
    try:
        response = requests.get(f"{BACKEND_URL}/test", timeout=10)
        print(f"✅ Backend connection: {response.status_code}")
        return True
    except Exception as e:
        print(f"❌ Backend connection failed: {e}")
        return False

def test_resume_parsing():
    """Test resume parsing with sample text"""
    sample_resume = """
John Doe
Software Engineer
john.doe@email.com

SKILLS
JavaScript, Python, React, Node.js, SQL

EXPERIENCE
Software Engineer | TechCorp | 2022-Present
• Built web applications using React and Node.js
• Implemented RESTful APIs

PROJECTS
E-commerce Platform | github.com/johndoe/ecommerce
• Full-stack application with React and Node.js
"""
    
    try:
        response = requests.post(
            f"{BACKEND_URL}/test-parse",
            json={"resume_text": sample_resume},
            timeout=30
        )
        
        print(f"Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Resume parsing successful!")
            print(f"Name: {data['data']['name']}")
            print(f"Skills count: {len(data['data']['skills']['skills'])}")
            print(f"Experience count: {len(data['data']['experience'])}")
            print(f"Projects count: {len(data['data']['projects'])}")
            return True
        else:
            print(f"❌ Resume parsing failed: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🚀 Testing resume parsing fix...\n")
    
    if test_backend_connection():
        test_resume_parsing()
    
    print("\n✨ Test completed!")

if __name__ == "__main__":
    main() 