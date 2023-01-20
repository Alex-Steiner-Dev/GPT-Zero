from flask import Flask, render_template
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/evaluate', methods = ['POST'])
def evaluation():
    return render_template("evaluate.html", result=evaluate(text))

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')