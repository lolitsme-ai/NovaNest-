from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "NovaNest AI Running 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # Simple AI reply (we upgrade later)
    reply = f"You said: {user_message}"
    
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
