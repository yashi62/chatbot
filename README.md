# Advanced Chatbot

A robust Python-based chatbot using Flask and OpenAI GPT-3.5 with features like user authentication, rate limiting, and structured logging.

## Features
- Intelligent chatbot responses using OpenAI GPT-3.5.
- User authentication with API keys.
- Rate limiting to prevent abuse.
- Logging for debugging and monitoring.

## Setup

### Prerequisites
- Python 3.8 or higher.
- OpenAI API key.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/advanced_chatbot.git
   cd advanced_chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your OpenAI API key in `services.py`:
   ```python
   openai.api_key = "your_openai_api_key_here"
   ```

4. Run the server:
   ```bash
   python app.py
   ```

### Usage
1. Send a POST request to the `/api/v1/chat` endpoint:
   ```bash
   curl -X POST -H "Content-Type: application/json" -H "Authorization: valid_api_key_1"    -d '{"message": "Hello, chatbot!"}' http://127.0.0.1:5000/api/v1/chat
   ```

## License
MIT
