# Import Flask, render_template, request from the flask pramework package :

from flask import Flask, render_template, request

# Import the emotion_detection function from the package created:

from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the dict and the dominant
        emotion for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    response_str = f"For the given statement, the system response is 'anger': {response['anger']}, "
    response_str +=  f"'disgust': {response['disgust']}, "
    response_str +=  f"'fear': {response['fear']}, "
    response_str +=  f"'joy': {response['joy']}, "
    response_str +=  f"'sadness': {response['sadness']}. "
    response_str +=  f"'The dominant emotion is <b>{response['dominant_emotion']}</b>."
    return response_str

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0",port=5000)