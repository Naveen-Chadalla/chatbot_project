from flask import Flask, render_template, request
import google.generativeai as genai
from config import API_KEY

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Initialize the model (use the one that worked for you earlier)
model = genai.GenerativeModel("gemini-1.5-pro")

# Create Flask app
app = Flask(__name__)

# Home route - displays the chatbot interface
@app.route("/")
def home():
    return render_template("index.html")

# Chat route - processes user messages
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    response = model.generate_content(user_message)
    return response.text  # Send back AI response

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
