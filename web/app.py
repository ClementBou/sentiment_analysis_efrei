from flask import Flask, render_template, request, redirect, url_for
from predict import predict
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence_requested = request.form['entry']
        sentence = []
        sentence.append(sentence_requested)
        return redirect(url_for('index', result=predict(sentence)))
      
    prediction = request.args.get('result')
    if prediction is None:
        return render_template('index.html')
    return render_template('index.html', result=prediction)