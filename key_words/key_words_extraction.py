import jieba
jieba.lcut('')
from jieba import analyse
import jieba.posseg as pseg


class KeywordExtractor:
    instances = None

    @classmethod
    def init(cls, models):
        if cls.instances is None:
            cls.instances = {}
        for model_name in models:
            cls.instances[model_name] = KeywordExtractor(model_name)

    def __init__(self, model_name):
        if model_name == 'tfidf':
            self.model = analyse.extract_tags
        elif model_name == 'textrank':
            self.model = analyse.textrank
        else:
            raise NotImplementedError('Extractor not supported!')

    def extract(self, text, num=5, pos=None):
        res = self.model(text, num)
        if pos is not None:
            words = pseg.cut(text)
            w2p = {word.word: word.flag for word in words}

            final_res = []
            for kw in res:
                if w2p.get(kw) in pos:
                    final_res.append(kw)
            return final_res
        return res

    @classmethod
    def get_instance(cls, model_name):
        instance = cls.instances.get(model_name)
        if instance is None:
            raise NotImplementedError
        return instance
