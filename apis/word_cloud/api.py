import logging
import os

from flask import request, render_template


from apis.nlpblueprint import NLPBlueprint
from apis.nlpexception import InvalidInputException, NLPException
from apis import utils

from visualization.word_cloud.plot import WordCloudVis

logger = logging.getLogger(__name__)


def init_word_cloud():
    global plotter
    plotter = WordCloudVis()


def init():
    logger.info('NLP word cloud API initializing...')
    init_word_cloud()


api_bp = NLPBlueprint('word_cloud', __name__, init, url_prefix='/nlp/v1/word_cloud')


@api_bp.route("/plot", methods=["GET", "POST"])
def word_cloud():
    if request.method == 'GET':
        text = request.args.get('text')
    elif request.method == 'POST':
        body = utils.get_body()
        text = body.get('text', None)
    else:
        text = None
    if text is None:
        return InvalidInputException("Parameter 'text' not found in request body")

    try:
        _name = plotter.word_cloud(text)
        return render_template('vis/word_cloud/{}.html'.format(_name))
    except Exception as e:
        print(e)
        return "Render error!"
