import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if the key is loaded correctly
if API_KEY:
    print("API Key loaded successfully!")
else:
    print("Error: API Key not found.")
