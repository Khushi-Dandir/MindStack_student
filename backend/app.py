from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from knowledge import INTENTS

app = Flask(__name__)
CORS(app)  # temporarily allow all origins for testing

@app.route("/")
def home():
    return "Backend running OK"

def get_response(user_message):
    try:
        user_message = user_message.lower().strip()
        for intent in INTENTS.values():
            for keyword in intent["keywords"]:
                if keyword in user_message:
                    return random.choice(intent["responses"])
    except Exception as e:
        print("Error in get_response:", e)

    # default supportive response
    return random.choice([
        "I'm here for you 💙 You can tell me more about how you're feeling.",
        "It's okay if you can't explain it clearly. Take your time 🌱",
        "I may not fully understand yet, but I’m listening 🤍",
        "That sounds difficult. Do you want to talk more about it?"
    ])

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        user_message = data.get("message", "")
        reply = get_response(user_message)
        return jsonify({"response": reply})
    except Exception as e:
        print("Error in /chat:", e)
        return jsonify({"response": "Sorry, something went wrong 😔"}), 500

if __name__ == "__main__":
    app.run(debug=True)
