from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import random
from knowledge import INTENTS
import os

# Use an absolute path for the frontend folder so Flask can always find files
FRONTEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
app = Flask(__name__, static_folder=FRONTEND_PATH)
CORS(app)  # for testing 


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


# Serve frontend static assets (css/js)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"response": "Please type something 🙂"})
 
    user_message = data["message"]
    reply = get_responses(user_message)

    return jsonify({"response": reply})


def get_responses(user_message):
    """Return an appropriate response from INTENTS or a supportive default."""
    user_message = (user_message or "").lower().strip()

    for intent in INTENTS.values():
        for keyword in intent.get("keywords", []):
            if keyword in user_message:
                return random.choice(intent.get("responses", []))

    return random.choice([
        "I'm here for you 💙 You can tell me more about how you're feeling.",
        "It's okay if you can't explain it clearly. Take your time 🌱",
        "I may not fully understand yet, but I’m listening 🤍",
        "That sounds difficult. Do you want to talk more about it?"
    ])
