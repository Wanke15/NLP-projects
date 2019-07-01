import logging
from flask import request


from apis.nlpblueprint import NLPBlueprint
from apis.nlpresponse import NLPResponse
from apis.nlpexception import InvalidInputException
from apis import utils

from sentiment_analysis.sentiment import SentimentPipeline

logger = logging.getLogger(__name__)


def init_sentiment():
    count_vec_path = 'resources/models/sentiment_analysis/count_vectorizer.m'
    classifier_path = 'resources/models/sentiment_analysis/classifier.m'
    stop_words_path = 'resources/data/中文停用词表.txt'
    SentimentPipeline.init(count_vec_path, classifier_path, stop_words_path)


def init():
    logger.info('NLP sentiment analysis API initializing...')
    init_sentiment()


api_bp = NLPBlueprint('sentiment', __name__, init, url_prefix='/nlp/v1/sentiment')


@api_bp.route("/analyse", methods=["GET", "POST"])
def words_segment():
    if request.method == 'GET':
        sentence = request.args.get('sentence')
    elif request.method == 'POST':
        body = utils.get_body()
        sentence = body.get('sentences', None)
    else:
        sentence = None
    if sentence is None:
        raise InvalidInputException("Parameter 'sentence' not found in request body")

    results = SentimentPipeline.predict(sentence=sentence)
    return NLPResponse(results, 200)
