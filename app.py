import logging
from flask import Flask, render_template, request, jsonify
from models import openai_api

app = Flask(__name__)

# Configure logging: log DEBUG and above levels to console and file.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("server.log")  # Log to file
    ]
)

@app.route('/')
def index():
    app.logger.info("Rendering index page")
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        app.logger.debug("Received data: %s", data)
        user_message = data.get("message", "")
        app.logger.info("User message: %s", user_message)
        
        response_text = openai_api.get_response(user_message)
        app.logger.info("Response generated: %s", response_text)
        
        return jsonify({"response": response_text})
    except Exception as e:
        app.logger.exception("Error in /api/chat endpoint")
        return jsonify({"error": "An error occurred processing your request."}), 500

if __name__ == '__main__':
    app.logger.info("Starting Flask server")
    app.run(debug=True)
