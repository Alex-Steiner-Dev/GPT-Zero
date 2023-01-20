from flask import Flask
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    evaluate(text)
    return 'Evaluation'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')