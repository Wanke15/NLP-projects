from sklearn.externals import joblib
import jieba


class Sentiment:
    def __init__(self):
        self.count_vec = None
        self.classifier = None
        self.stop_words = None
        self.class_dict = {0: '消极', 1: '积极'}

    def preprocess(self, sentence):
        if not isinstance(sentence, list):
            sentence = list(sentence)
        return_data = []
        for record in sentence:
            _tmp = jieba.lcut(record)
            return_data.append(" ".join([_ for _ in _tmp if _ not in self.stop_words]))
        return return_data
    
    def load(self, count_vec_path, classifier_path, stop_words_path):
        self.count_vec = joblib.load(count_vec_path)
        self.classifier = joblib.load(classifier_path)

        with open(stop_words_path, 'r', encoding='utf8') as f:
            stop_words = f.readlines()
            self.stop_words = [_.strip() for _ in stop_words]

    def predict(self, sentence):
        sentence = self.preprocess(sentence)
        sentence_vec = self.count_vec.transform(sentence)

        predicted = self.classifier.predict(sentence_vec)

        return {'sentiment': self.class_dict.get(predicted[0])}
