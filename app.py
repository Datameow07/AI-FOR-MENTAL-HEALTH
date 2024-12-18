import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Set up Hugging Face API token securely using environment variable
api_token = os.getenv('HF_API_KEY')  # Never hardcode API key
headers = {
    "Authorization": f"Bearer {api_token}"
}

# Define the Hugging Face API URL for the model
model_url = "https://api-inference.huggingface.co/models/rasa/cmd_gen_codellama_13b_calm_demo"

# Function to query the Hugging Face model
def query_model(user_input):
    data = {
        "inputs": user_input,
    }
    
    response = requests.post(model_url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code}, {response.text}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=["POST"])
def chat():
    user_input = request.form['message']
    bot_response = query_model(user_input)
    return render_template('index.html', user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)