from sklearn.externals import joblib


class SentimentModel:
    def __init__(self, count_vec_path, classifier_path):
        self.count_vec = joblib.load(count_vec_path)
        self.classifier = joblib.load(classifier_path)

        self.class_dict = {0: '消极', 1: '积极'}

    def process(self, sentence):
        request_feat = self.count_vec.transform(sentence)
        predicted = self.classifier.predict(request_feat)
        return predicted
