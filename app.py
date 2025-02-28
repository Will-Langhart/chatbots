from flask import Flask, render_template, request, jsonify
from models import openai_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response_text = openai_api.get_response(user_message)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
