import jieba
import logging

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
            logger.warning("'cut_all':{} arg not recognized".format(cut_all))
            cut_all = False
        result = jieba.lcut(sentence, cut_all)
        return {"results": result}
