import os
from google import genai

# This fetches your secret key from the GitHub 'safe'
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the new 2026 Client
client = genai.Client(api_key=api_key)

# We are using Gemini 3 Flash, the current balanced model for 2026
response = client.models.generate_content(
    model="gemini-3-flash", 
    contents="I am building a news scraper. Say 'The Brain is Online!' if you can hear me."
)

print(response.text)
