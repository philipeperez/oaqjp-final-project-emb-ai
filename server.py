from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] == None:
        return '<b>Invalid text! Please try again!</b>', 400

    response_text = f"For the given statement, the system response is 'anger': {res['anger']}, 'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}. The dominant emotion is <b>{res['dominant_emotion']}</b>."

    return response_text

if __name__ == "__main__":
    app.run(port=5000, debug=True)