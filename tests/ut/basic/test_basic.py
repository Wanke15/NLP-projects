import unittest

from basic.words_segment import Segmentor


class TestBasic(unittest.TestCase):
    def test_words_segment(self):
        results = Segmentor.segment("我爱中华人民共和国", 'false')
        self.assertEqual(3, len(results['results']))

        results = Segmentor.segment("我爱中华人民共和国", 'true')
        self.assertEqual(10, len(results['results']))
