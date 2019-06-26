from flask import Flask

app = Flask(__name__)


@app.route('/nlp/v1/health', methods=['GET'])
def hello():
    return "I'm doing great!"
