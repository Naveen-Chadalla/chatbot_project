import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)

# Use an available model name from your list
model = genai.GenerativeModel("gemini-1.5-pro")

response = model.generate_content("Hello! How are you?")
print("Gemini Response:", response.text)
