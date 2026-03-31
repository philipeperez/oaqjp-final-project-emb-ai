"""Flask application for emotion detection.

This module exposes HTTP endpoints to render a homepage and analyze
user-provided text to detect emotions using the EmotionDetection service.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the home page.

    Returns:
        str: Rendered HTML template for the homepage.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """Analyze text and return detected emotions.

    This endpoint receives a query parameter `textToAnalyze`,
    processes it using the emotion detector, and returns a
    formatted string with emotion scores and the dominant emotion.

    Query Params:
        textToAnalyze (str): The input text to analyze.

    Returns:
        str: A formatted string containing emotion analysis results.

    Raises:
        400: If the input text is invalid or no dominant emotion is detected.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] is None:
        return '<b>Invalid text! Please try again!</b>', 400

    response_text = f"For the given statement,\
     the system response is 'anger': {res['anger']},\
      'disgust': {res['disgust']}, 'fear': {res['fear']},\
       'joy': {res['joy']} and 'sadness': {res['sadness']}.\
        The dominant emotion is <b>{res['dominant_emotion']}</b>."

    return response_text

if __name__ == "__main__":
    app.run(port=5000, debug=True)
