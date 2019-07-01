import jieba


class SentimentPreprocessor:
    def __init__(self, stop_words_path):

        with open(stop_words_path, 'r', encoding='utf8') as f:
            stop_words = f.readlines()
            self.stop_words = [_.strip() for _ in stop_words]

    def preprocess(self, sentence):
        if not isinstance(sentence, list):
            sentence = list(sentence)
        return_data = []
        for record in sentence:
            _tmp = jieba.lcut(record)
            return_data.append(" ".join([_ for _ in _tmp if _ not in self.stop_words]))
        return return_data
