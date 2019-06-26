import logging
from flask import request


from apis.nlpblueprint import NLPBlueprint
from apis.nlpresponse import NLPResponse

from basic.words_segment import Segmentor

logger = logging.getLogger(__name__)


def init_ws():
    Segmentor.segment("我爱中华人民共和国")


def init():
    logger.info('NLP API initializing...')
    init_ws()


api_bp = NLPBlueprint('basic', __name__, init, url_prefix='/nlp/v1/basic')


@api_bp.route("/words_segment", methods=["GET"])
def words_segment():
    sentence = request.args.get('sentence', '')
    cut_all = request.args.get('cut_all', 'false')

    results = Segmentor.segment(sentence, cut_all)
    return NLPResponse(results, 200)
