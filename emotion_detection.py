def emotion_detector(text):
    if text == "":
        return {"error": "Invalid input"}
    
    return {
        "anger": 0.1,
        "joy": 0.8,
        "sadness": 0.1,
        "fear": 0.0,
        "disgust": 0.0
    }
