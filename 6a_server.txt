from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector") 
def emotion_detection_route(): # Retrieve the text to analyze from the request arguments 
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the sentiment_analyzer function and store the response 
    result = emotion_detector(text_to_analyze)

    if result is None or result.get('dominant_emotion') is None:
        return "Invalid text! Please try again."
    
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000) 