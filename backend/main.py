from flask import Flask, request, jsonify
from chatbot.engine import ChatbotEngine

app = Flask(__name__)
chatbot = ChatbotEngine(user_id="vinicius")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
