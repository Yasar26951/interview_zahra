from flask import Flask, request, jsonify
from flask cors import CORS
from langchain_core.messages import HumanMessage
from agent import app1

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    result = app1. invoke({
        "history": [HumanMessage(content=user_input)]})

    return jsonify({
        "response": result["history"][-1].content})

if __name__=="__main__":
    app.run(debug=True)