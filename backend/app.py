from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

JENKINS_URL = os.getenv("JENKINS_URL")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")
JENKINS_JOB = os.getenv("JENKINS_JOB")

def trigger_jenkins():
    url = f"{JENKINS_URL}/job/{JENKINS_JOB}/build"
    response = requests.post(url, auth=(JENKINS_USER, JENKINS_TOKEN))
    return response.status_code

@app.route("/")
def home():
    return "🚀 DevOps Deck Backend is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 GitHub Webhook Received!")
    
    status = trigger_jenkins()
    
    if status == 201:
        return "✅ Jenkins triggered", 200
    else:
        return "❌ Failed to trigger Jenkins", 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
