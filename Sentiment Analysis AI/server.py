
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    '''
    This view function receives text from the HTML interface and
    performs sentiment analysis using sentiment_analyzer().
    It returns the label and its confidence score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input! Try again."
    #else:
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    '''
    This function renders the html document with appropriate message.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=5001)


# run this using "python3.11 server.py"
