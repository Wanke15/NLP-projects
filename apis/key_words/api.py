import logging

from flask import request

from apis.nlpblueprint import NLPBlueprint
from apis.nlpresponse import NLPResponse

from key_words.key_words_extraction import KeywordExtractor

logger = logging.getLogger(__name__)


def init_kw():
    KeywordExtractor.init(['tfidf', 'textrank'])


def init():
    logger.info('NLP key words API initializing...')
    init_kw()


api_bp = NLPBlueprint('key_words', __name__, init, url_prefix='/nlp/v1/key_words')


@api_bp.route("/extract", methods=["GET"])
def extract_key_words():
    extractor = request.args.get('extractor', 'tfidf')
    text = request.args.get('text', '')
    num = int(request.args.get('num', 5))
    pos = request.args.get('pos', None)

    results = KeywordExtractor.get_instance(extractor).extract(text, num, pos)
    return NLPResponse(results, 200)
