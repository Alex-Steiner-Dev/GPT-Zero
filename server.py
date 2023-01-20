from flask import Flask, render_template, request
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/evaluate", methods=['GET', 'POST'])
def evaluation():
    if request.method == 'POST':
        return render_template("evaluate.html", result=evaluate(request.form['text-area']))

    elif request.method == 'GET':
        print("No Post Back Call")

    return render_template("index.html")
    

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')