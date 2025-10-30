from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def home():
    return "✅ Bot ishlayapti!"

@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    message = f"📊 Signal keldi!\nPair: {data.get('ticker')}\nAction: {data.get('action')}"
    send_to_telegram(message)
    return "OK", 200

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
