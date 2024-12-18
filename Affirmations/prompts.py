from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from textblob import TextBlob
import random

app = Flask(__name__)
CORS(app)  # To handle cross-origin requests from the frontend

# Define affirmations for each sentiment
affirmations = {
    "positive": [
        "I am capable of achieving my goals.",
        "I radiate positivity and energy.",
        "Every day I grow stronger and better.",
        "I am worthy of success and happiness.",
        "I believe in myself and my abilities."
    ],
    "neutral": [
        "I trust the journey and process of life.",
        "I am learning and growing every day.",
        "Every challenge is a chance to improve.",
        "I am open to new experiences and opportunities.",
        "I am doing my best, and that is enough."
    ],
    "negative": [
        "I am stronger than any challenge I face.",
        "This moment will pass, and I will feel better.",
        "I am in control of my thoughts and feelings.",
        "I am worthy of love and peace.",
        "I choose to release negative thoughts and embrace positivity."
    ]
}

# Route to render the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to analyze sentiment and return affirmations
@app.route('/get_affirmations', methods=['POST'])
def get_affirmations():
    journal_entry = request.json.get('journal_entry', '')
    
    if journal_entry:
        # Perform sentiment analysis using TextBlob
        blob = TextBlob(journal_entry)
        sentiment = blob.sentiment.polarity  # Sentiment polarity (-1 to 1)
        
        # Determine sentiment category
        if sentiment > 0.1:
            sentiment_category = "positive"
        elif sentiment < -0.1:
            sentiment_category = "negative"
        else:
            sentiment_category = "neutral"
        
        # Select 5 random affirmations based on the sentiment
        selected_affirmations = random.sample(affirmations[sentiment_category], 5)
        return jsonify({"affirmations": selected_affirmations})
    
    return jsonify({"error": "No journal entry provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
