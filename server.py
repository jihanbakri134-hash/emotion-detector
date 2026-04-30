from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect():
    text = request.args.get("text")
    
    if text == "":
        return "Invalid input", 400
    
    result = emotion_detector(text)
    return jsonify(result)

app.run(host="0.0.0.0", port=5000)
