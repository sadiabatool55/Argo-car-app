from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Auto Scaling Cars App Running 🚗"

@app.route("/replicas")
def replicas():
    hostname = socket.gethostname()
    return jsonify({
        "pod": hostname
    })

@app.route("/load")
def load():
    while True:
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
