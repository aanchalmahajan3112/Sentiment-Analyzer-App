import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']

    if(score > 0):
        label = 'Positive Sentiment'

    elif(score == 0):
        label = 'Neutral Sentiment'

    else:
        label = 'Negative Sentiment'

    return(render_template('index.html', variable=label))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)