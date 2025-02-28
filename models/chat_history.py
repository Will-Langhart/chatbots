# models/chat_history.py

# This module can be used to manage conversation history.
chat_history = []

def add_message(user_message, bot_response):
    chat_history.append({
        "user": user_message,
        "bot": bot_response
    })

def get_history():
    return chat_history
