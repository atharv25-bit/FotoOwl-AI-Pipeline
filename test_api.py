import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ GOOGLE_API_KEY not found in .env")
    exit()

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content("Say Hello")

    print("✅ API Connected Successfully!")
    print("Response:")
    print(response.text)

except Exception as e:
    print("❌ API Connection Failed")
    print(e)