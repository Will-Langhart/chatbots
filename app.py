from flask import Flask, render_template, request, jsonify
from models import openai_api, pinecone

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    
    # Get response from OpenAI (or a multi-LLM pipeline)
    response_text = openai_api.get_response(user_message)
    
    # Optionally, store vector representation in Pinecone for future retrieval
    pinecone.store_vector(user_message)
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
