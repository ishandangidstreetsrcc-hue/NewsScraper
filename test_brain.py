import os
from google import genai

# Fetch the key
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

try:
    # 1. THE TEST: Using Gemini 2.5 Flash (The current stable standard)
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents="I am building a news scraper. Say 'The Brain is Online!' if you can hear me."
    )
    print(f"--- TEST RESULT ---\n{response.text}\n")

    # 2. THE DEBUG: Let's see what Gemini 3 models are actually called for your key
    print("--- AVAILABLE MODELS ---")
    for m in client.models.list():
        if "gemini" in m.name:
            print(m.name)

except Exception as e:
    print(f"An error occurred: {e}")
