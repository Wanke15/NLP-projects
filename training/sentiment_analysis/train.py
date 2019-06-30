import pandas as pd

import jieba

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split

from sklearn.externals import joblib

from sklearn.naive_bayes import MultinomialNB


def load_data(pos_path='training/sentiment_analysis/data/pos.xls', neg_path='training/sentiment_analysis/data/neg.xls'):
    neg_data = pd.read_excel(neg_path, header=None).iloc[:, 0]
    pos_data = pd.read_excel(pos_path, header=None).iloc[:, 0]

    _data = []
    _data.extend(pos_data)
    _data.extend(neg_data)

    _targets = []
    _targets.extend([1 for _ in range(len(pos_data))])
    _targets.extend([0 for _ in range(len(neg_data))])

    return _data, _targets


data, targets = load_data()
assert len(data) == len(targets), 'data and targets number not equal'

with open('training/sentiment_analysis/data/中文停用词表.txt', 'r', encoding='utf8') as f:
    stop_words = f.readlines()
    stop_words = [_.strip() for _ in stop_words]


def preprocess(new_data):
    return_data = []
    for record in new_data:
        _tmp = jieba.lcut(record)
        return_data.append(" ".join([_ for _ in _tmp if _ not in stop_words]))
    return return_data

# data_segs = []
# for record in data:
#     _tmp = jieba.lcut(record)
#     data_segs.append(" ".join([_ for _ in _tmp if _ not in stop_words]))

data_segs = preprocess(data)

x_train, x_test, y_train, y_test = train_test_split(data_segs, targets, test_size=0.2, random_state=101)

count_vect = CountVectorizer()
data_counts = count_vect.fit_transform(data)

# tfidf_transformer = TfidfTransformer()
# tfidf_transformer.fit_transform(data_counts)

X_train_tfidf = count_vect.transform(x_train)

clf = MultinomialNB().fit(X_train_tfidf, y_train)

print(clf.score(X_train_tfidf, y_train))

X_test_tfidf = count_vect.transform(x_test)
print(clf.score(X_test_tfidf, y_test))

docs_new = ['我很喜欢这件商品', '东西还没试过，但感觉赠品有点垃圾', '新买的这本书真不错，下次还去这家店铺']
docs_new_seg = preprocess(docs_new)

X_new_tfidf = count_vect.transform(docs_new_seg)

predicted = clf.predict(X_new_tfidf)

print(predicted)


joblib.dump(count_vect, 'resources/models/sentiment_analysis/count_vectorizer.m')
joblib.dump(clf, 'resources/models/sentiment_analysis/classifier.m')