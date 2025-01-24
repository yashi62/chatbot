from flask import Flask, request, jsonify
from chatbot.authentication import authenticate_user
from chatbot.services import generate_reply
from chatbot.rate_limiter import RateLimiter
from chatbot.logger import setup_logging

app = Flask(__name__)

# Initialize logging
setup_logging()

# API rate limiter
rate_limiter = RateLimiter(max_requests=5, time_window=60)

@app.route('/api/v1/chat', methods=['POST'])
def chat():
    # Authenticate user
    api_key = request.headers.get('Authorization')
    if not authenticate_user(api_key):
        return jsonify({'error': 'Unauthorized'}), 401

    # Enforce rate limiting
    if not rate_limiter.is_allowed(api_key):
        return jsonify({'error': 'Rate limit exceeded. Try again later.'}), 429

    # Process user message
    data = request.json
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400

    bot_response = generate_reply(user_message)
    return jsonify({'user_message': user_message, 'bot_response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
