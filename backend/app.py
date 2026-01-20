from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import random
from knowledge import INTENTS
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app)  # testing ke liye

# Serve frontend
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        user_message = data.get("message", "")
        for intent in INTENTS.values():
            for keyword in intent["keywords"]:
                if keyword in user_message.lower():
                    return jsonify({"response": random.choice(intent["responses"])})
        return jsonify({"response": "I'm listening 💙"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "Something went wrong 😔"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
