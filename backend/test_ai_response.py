#!/usr/bin/env python3
"""
Test script to debug AI response and JSON parsing issues
"""

import os
import json
import re
import groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("❌ GROQ_API_KEY not found in environment variables")
    exit(1)

groq_client = groq.Groq(api_key=GROQ_API_KEY)

# Test resume text
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

def test_ai_response():
    """Test the AI response directly"""
    print("🤖 Testing AI response...")
    
    prompt = f"""
You are an expert resume parsing system. Extract information from the following resume text and format it as a valid JSON object.
Adhere strictly to this JSON schema. Do not add any extra text or explanations.

Schema:
{{
  "name": "string",
  "skills": {{
    "skills": ["string", "string", ...]
  }},
  "experience": [
    {{
      "title": "string",
      "company": "string",
      "duration": "string",
      "description": "string",
      "achievements": ["string", "string", ...]
    }}
  ],
  "projects": [
    {{
      "title": "string",
      "description": "string",
      "link": "string"
    }}
  ]
}}

Resume Text:
\"\"\"
{TEST_RESUME_TEXT}
\"\"\"
"""

    try:
        # Call the AI
        chat_completion = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are an expert resume parsing system. You must return ONLY valid JSON that strictly follows the provided schema. Do not include any explanatory text, markdown formatting, or additional content outside the JSON object."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )

        content = chat_completion.choices[0].message.content
        
        print("📄 Raw AI Response:")
        print("=" * 50)
        print(content)
        print("=" * 50)
        
        # Test the cleaning logic
        print("\n🧹 Testing JSON cleaning...")
        
        # Clean the response more thoroughly
        cleaned = re.sub(r"^```(?:json)?|```$", "", content.strip(), flags=re.MULTILINE)
        cleaned = re.sub(r'^.*?\{', '{', cleaned, flags=re.DOTALL)
        
        # Find the last complete JSON object by counting braces
        brace_count = 0
        json_end = -1
        for i, char in enumerate(cleaned):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    json_end = i + 1
                    break
        
        if json_end > 0:
            cleaned = cleaned[:json_end]
        
        # Additional cleaning for common AI response patterns
        cleaned = re.sub(r'^Here is the JSON.*?\{', '{', cleaned, flags=re.DOTALL | re.IGNORECASE)
        cleaned = re.sub(r'^The extracted information.*?\{', '{', cleaned, flags=re.DOTALL | re.IGNORECASE)
        
        print("Cleaned content:")
        print("=" * 50)
        print(cleaned)
        print("=" * 50)
        
        # Test JSON parsing
        print("\n🔍 Testing JSON parsing...")
        try:
            parsed = json.loads(cleaned)
            print("✅ JSON parsing successful!")
            print(f"Parsed data keys: {list(parsed.keys())}")
            print(f"Name: {parsed.get('name', 'Not found')}")
            print(f"Skills count: {len(parsed.get('skills', {}).get('skills', []))}")
            print(f"Experience count: {len(parsed.get('experience', []))}")
            print(f"Projects count: {len(parsed.get('projects', []))}")
            
            # Pretty print the full response
            print("\n📋 Full parsed data:")
            print(json.dumps(parsed, indent=2))
            
        except json.JSONDecodeError as e:
            print(f"❌ JSON parsing failed: {e}")
            print(f"Error position: {e.pos}")
            print(f"Error line: {e.lineno}")
            print(f"Error column: {e.colno}")
            
            # Show the problematic part
            if e.pos < len(cleaned):
                start = max(0, e.pos - 50)
                end = min(len(cleaned), e.pos + 50)
                print(f"Context around error:")
                print(cleaned[start:end])
                print(" " * (e.pos - start) + "^")
        
    except Exception as e:
        print(f"❌ AI request failed: {e}")

def main():
    """Run the test"""
    print("🚀 Starting AI response test...\n")
    test_ai_response()
    print("\n✨ Test completed!")

if __name__ == "__main__":
    main() 