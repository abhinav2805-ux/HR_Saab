#!/usr/bin/env python3
"""
Simple test to check the exact response format from the backend
"""

import requests
import json

def test_parse_resume_response():
    """Test the exact response format from parse-resume endpoint"""
    
    # Create a simple test file
    test_content = b"John Doe\nSoftware Engineer\njohn.doe@email.com\n\nSKILLS\nJavaScript, Python, React\n\nEXPERIENCE\nSoftware Engineer | TechCorp | 2022-Present\n• Built web applications\n\nPROJECTS\nE-commerce Platform | github.com/johndoe/ecommerce\n• Full-stack application"
    
    try:
        # Test the actual parse-resume endpoint
        files = {'resume': ('test.docx', test_content, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')}
        
        response = requests.post(
            'https://hr-saab.onrender.com/parse-resume',
            files=files,
            timeout=30
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Content-Type: {response.headers.get('content-type', 'Not set')}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ Success! Response data:")
                print(json.dumps(data, indent=2))
                
                # Check the structure
                if isinstance(data, dict):
                    print(f"✅ Response is a dictionary with keys: {list(data.keys())}")
                    if 'name' in data:
                        print(f"✅ Name field present: {data['name']}")
                    if 'skills' in data:
                        print(f"✅ Skills field present: {type(data['skills'])}")
                    if 'experience' in data:
                        print(f"✅ Experience field present: {type(data['experience'])}")
                    if 'projects' in data:
                        print(f"✅ Projects field present: {type(data['projects'])}")
                else:
                    print(f"❌ Response is not a dictionary: {type(data)}")
                    
            except json.JSONDecodeError as e:
                print(f"❌ JSON decode error: {e}")
                print(f"Raw response: {response.text}")
        else:
            print(f"❌ Error response: {response.status_code}")
            print(f"Error text: {response.text}")
            
    except Exception as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    print("🔍 Testing parse-resume endpoint response format...\n")
    test_parse_resume_response()
    print("\n✨ Test completed!") 