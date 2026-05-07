import os
import google.generativeai as genai

# This gets your secret key from the GitHub 'safe'
api_key = os.getenv("GEMINI_API_KEY")

# Set up the AI
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Ask it a question
response = model.generate_content("I am building a news scraper. Say 'The Brain is Online!' if you can hear me.")

print(response.text)
