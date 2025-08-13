#!/usr/bin/env python3
"""
Test the deployed backend after API key update
"""

import requests
import json
import time

def test_deployment():
    """Test the deployed backend"""
    print("🔍 Testing deployed backend...")
    
    # Test 1: Health check
    try:
        response = requests.get("https://hr-saab.onrender.com/test", timeout=10)
        print(f"✅ Health check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend response: {data}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False
    
    # Test 2: Resume parsing
    print("\n📄 Testing resume parsing...")
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
    
    try:
        response = requests.post(
            "https://hr-saab.onrender.com/test-parse",
            json={"resume_text": test_resume},
            timeout=60
        )
        
        print(f"📥 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Resume parsing successful!")
            print(f"✅ Success: {data.get('success', False)}")
            if data.get('success') and data.get('data'):
                parsed_data = data['data']
                print(f"✅ Name: {parsed_data.get('name', 'Not found')}")
                print(f"✅ Skills count: {len(parsed_data.get('skills', {}).get('skills', []))}")
                print(f"✅ Experience count: {len(parsed_data.get('experience', []))}")
                print(f"✅ Projects count: {len(parsed_data.get('projects', []))}")
            return True
        else:
            print(f"❌ Resume parsing failed: {response.status_code}")
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    print("🚀 Testing Deployed Backend After API Key Update\n")
    
    # Give some time for deployment to complete
    print("⏳ Waiting 30 seconds for deployment to complete...")
    time.sleep(30)
    
    success = test_deployment()
    
    print("\n" + "="*50)
    if success:
        print("🎉 SUCCESS! Your resume parser is now working!")
        print("\n✅ Next steps:")
        print("1. Go to your frontend application")
        print("2. Click '🔍 Test Backend Connection'")
        print("3. Upload a resume file")
        print("4. It should parse successfully!")
    else:
        print("❌ Still having issues. Please check:")
        print("1. API key is correctly set in Render")
        print("2. Service has finished redeploying")
        print("3. Check Render logs for errors")

if __name__ == "__main__":
    main()
