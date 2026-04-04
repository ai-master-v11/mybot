from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Connector is Live!"

@app.route('/webhook', methods=['POST'])
def receive_signal():
    data = request.json
    if data:
        print("Signal Received:", data)
        return jsonify({"status": "Success"}), 200
    return "No Data", 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
