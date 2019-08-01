import unittest

from key_words.key_words_extraction import KeywordExtractor


class TestKeyWords(unittest.TestCase):
    def setUp(self):
        KeywordExtractor.init(['tfidf', 'textrank'])

    def test_tfidf(self):
        test_text = 'RAKE算法用来做关键词(keyword)的提取，实际上提取的是关键的短语(phrase)'
        res = KeywordExtractor.get_instance('tfidf').extract(test_text)
        print(res)

    def test_textrank(self):
        test_text = 'RAKE算法用来做关键词(keyword)的提取，实际上提取的是关键的短语(phrase)'
        res = KeywordExtractor.get_instance('textrank').extract(test_text)
        print(res)

    def test_use_pos(self):
        test_text = 'RAKE算法用来做关键词(keyword)的提取，实际上提取的是关键的短语(phrase)'
        pos = ['n', 'v']
        res = KeywordExtractor.get_instance('textrank').extract(test_text, pos=pos)
        print(res)

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError) as cm:
            KeywordExtractor.init(['tfidf', 'textrank', 'lda'])
        self.assertEqual(str(cm.exception), 'Extractor not supported!')
