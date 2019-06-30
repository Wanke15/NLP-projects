import logging
from flask import request


from apis.nlpblueprint import NLPBlueprint
from apis.nlpresponse import NLPResponse

from sentiment_analysis.sentiment import Sentiment

logger = logging.getLogger(__name__)


def init_sentiment():
    count_vec_path = 'resources/models/sentiment_analysis/count_vectorizer.m'
    classifier_path = 'resources/models/sentiment_analysis/classifier.m'
    stop_words_path = 'resources/models/sentiment_analysis/中文停用词表.txt'
    Sentiment.load(count_vec_path, classifier_path, stop_words_path)


def init():
    logger.info('NLP sentiment analysis API initializing...')
    init_sentiment()


api_bp = NLPBlueprint('basic', __name__, init, url_prefix='/nlp/v1/basic')


@api_bp.route("/words_segment", methods=["GET"])
def words_segment():
    sentence = request.args.get('sentence', '')
    cut_all = request.args.get('cut_all', 'false')

    results = Segmentor.segment(sentence, cut_all)
    return NLPResponse(results, 200)
