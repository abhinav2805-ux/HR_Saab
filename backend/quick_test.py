#!/usr/bin/env python3
"""
Quick test to verify Groq API is working
"""

import os
import groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_groq_api():
    """Test if Groq API is working"""
    print("🔍 Testing Groq API connection...")
    
    # Get API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ GROQ_API_KEY not found in environment variables")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...")
    
    try:
        # Initialize Groq client
        client = groq.Groq(api_key=api_key)
        
        # Test with a simple prompt
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": "Say 'Hello, Groq is working!' and nothing else."}
            ],
            temperature=0.1
        )
        
        content = response.choices[0].message.content
        print(f"✅ Groq API response: {content}")
        return True
        
    except Exception as e:
        print(f"❌ Groq API test failed: {e}")
        return False

def test_simple_resume_parsing():
    """Test resume parsing with minimal content"""
    print("\n📄 Testing simple resume parsing...")
    
    try:
        import requests
        
        # Simple test resume
        test_resume = """
John Doe
Software Engineer
john.doe@email.com

SKILLS
JavaScript, Python, React

EXPERIENCE
Software Engineer | TechCorp | 2022-Present
• Built web applications

PROJECTS
E-commerce Platform | github.com/johndoe/ecommerce
• Full-stack application
"""
        
        response = requests.post(
            "https://hr-saab.onrender.com/test-parse",
            json={"resume_text": test_resume},
            timeout=30
        )
        
        print(f"📥 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Simple parsing successful!")
            print(f"✅ Response: {data}")
            return True
        else:
            print(f"❌ Simple parsing failed: {response.status_code}")
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Quick Groq API Test\n")
    
    # Test 1: Groq API connection
    groq_working = test_groq_api()
    
    # Test 2: Simple resume parsing
    parsing_working = test_simple_resume_parsing()
    
    # Summary
    print("\n" + "="*50)
    print("📊 Test Summary:")
    print(f"✅ Groq API: {'PASS' if groq_working else 'FAIL'}")
    print(f"✅ Resume Parsing: {'PASS' if parsing_working else 'FAIL'}")
    
    if groq_working and parsing_working:
        print("\n🎉 Everything is working! Resume parsing should work now.")
    elif not groq_working:
        print("\n⚠️  Groq API is not working. Check your API key and credits.")
    else:
        print("\n⚠️  Groq API works but resume parsing fails. Check backend logs.")
