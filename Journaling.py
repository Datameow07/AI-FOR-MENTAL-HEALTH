from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Importing CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define categories and prompts
journaling_prompts = {
    "General": [
        "What are three things you’re grateful for today, and why?",
        "How are you feeling right now? Describe your emotions in detail.",
        "What’s one thing you accomplished today that made you proud?",
        "Write about a challenge you faced today. How did you handle it?",
        "What’s one thing you wish you could improve about today, and how can you work on it tomorrow?"
    ],
    "Stress and Anxiety": [
        "What is currently causing you stress? How can you take a small step to reduce it?",
        "Describe a situation where you felt anxious. What thoughts were going through your mind?",
        "What activities or moments in your day helped you feel calm or at ease?",
        "Write about a time when you overcame a stressful situation. What strategies worked for you?",
        "What is one thing you can do to take care of yourself when you feel overwhelmed?"
    ],
    "Self-Esteem and Confidence": [
        "List three qualities you love about yourself and why.",
        "What’s one moment recently when you felt truly confident? Describe it.",
        "If you were giving advice to your younger self, what would you say?",
        "Write about a compliment you received recently. How did it make you feel?",
        "What are your biggest strengths? How do they help you in your daily life?"
    ],
    "Loneliness": [
        "Describe a time when you felt truly connected to someone. What made that moment special?",
        "What is one way you can reach out to someone you care about this week?",
        "What does a 'perfect day' look like to you, and who would you want to share it with?",
        "Reflect on a relationship that’s meaningful to you. Why is it important?",
        "What are some ways you can enjoy your own company today?"
    ],
    "Emotional Healing": [
        "Write about a difficult experience you’re currently processing. How does it make you feel?",
        "What are some positive lessons you’ve learned from a tough situation in the past?",
        "What does forgiveness mean to you, and is there someone you need to forgive (including yourself)?",
        "If you could let go of one worry or fear, what would it be?",
        "What does healing look like to you, and what steps can you take toward it?"
    ],
    "Goal Setting and Motivation": [
        "What’s a personal goal you’re excited to work on? Why is it important to you?",
        "What are three small steps you can take toward achieving your goal this week?",
        "Reflect on a goal you’ve already achieved. What did you learn from the process?",
        "What motivates you to keep going when things get tough?",
        "If you had no limits, what’s one dream you would pursue today?"
    ],
}

# Route to render the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API to get prompts based on category
@app.route('/get_prompts', methods=['POST'])
def get_prompts():
    data = request.json
    category = data.get('category', '')
    if category in journaling_prompts:
        prompts = random.sample(journaling_prompts[category], k=2)  # Select 2 random prompts
        return jsonify({"prompts": prompts})
    else:
        return jsonify({"error": "Invalid category"}), 400

# Route to save journal entry
@app.route('/save_journal', methods=['POST'])
def save_journal():
    journal_entry = request.json.get('journal_entry', '')
    if journal_entry:
        with open("journals.txt", "a") as file:
            file.write(journal_entry + "\n\n")
        return jsonify({"message": "Journal entry saved successfully!"}), 200
    return jsonify({"error": "No journal entry provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
