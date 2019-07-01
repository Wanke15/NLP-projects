import os
import unittest

from apis.utils import get_base_dir

from sentiment_analysis.sentiment import SentimentPipeline


class TestBasic(unittest.TestCase):
    def test_init(self):
        base_dir = get_base_dir()
        count_vec_path = os.path.join(base_dir, 'resources/models/sentiment_analysis/count_vectorizer.m')
        classifier_path = os.path.join(base_dir, 'resources/models/sentiment_analysis/classifier.m')
        stop_words_path = os.path.join(base_dir, 'resources/data/中文停用词表.txt')
        SentimentPipeline.init(count_vec_path, classifier_path, stop_words_path)

    def test_analyse_get(self):
        self.test_init()
        sentence = "我拿这家店铺的老板一点办法都没有"
        results = SentimentPipeline.predict(sentence=sentence)
        print(results)

    def test_analyse_post(self):
        self.test_init()
        sentence = ["我拿这家店铺的老板一点办法都没有", "东西还没试过，但感觉赠品有点垃圾"]
        results = SentimentPipeline.predict(sentence=sentence)
        print(results)
