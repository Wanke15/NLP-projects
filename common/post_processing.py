class SentimentPostprocessor:
    def __init__(self):
        self.class_dict = {0: '消极', 1: '积极'}

    def post_process(self, sentence, predictor_result):
        result = [{'sentence': _sent, 'sentiment': self.class_dict.get(_class)}
                  for _sent, _class in zip(sentence, predictor_result)]
        return result
