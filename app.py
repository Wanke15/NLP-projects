from flask import Flask

app = Flask(__name__)


@app.route('/nlp/v1/health', methods=['GET'])
def hello():
    return "Jeff Wang's NLP project. I'm doing great!"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8001)
