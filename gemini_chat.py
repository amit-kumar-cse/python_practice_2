import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()
# Access environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
print("GEMINI_API_KEY: ", GEMINI_API_KEY)

# get env variable here in a variable
# Only run this block for Gemini Developer API
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash-001", 
    contents="why the mind wanders?"
)

print(response.text)
