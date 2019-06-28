import jieba
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format=
    '%(asctime)s %(levelname)s %(message)s',
    datefmt='%d %b %Y %H:%M:%S')

logger = logging.getLogger(__name__)


class Segmentor:
    def __init__(self):
        pass

    @classmethod
    def segment(cls, sentence, cut_all='false'):
        if cut_all == 'false':
            cut_all = False
        elif cut_all == 'true':
            cut_all = True
        else:
            logger.warning("cut_all => '{}' arg not recognized".format(cut_all))
            cut_all = False
        result = jieba.lcut(sentence, cut_all)
        return {"results": result}
