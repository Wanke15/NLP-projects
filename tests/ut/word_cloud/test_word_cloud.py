import os
from unittest import TestCase

from visualization.word_cloud.plot import WordCloudVis


class TestWordCloud(TestCase):
    def setUp(self):
        self.plotter = WordCloudVis()

    def test_render_html(self):
        text = "最底下是知识获取及存储，或者说是数据支持层，首先从不同来源、不同结构的数据中获取知识，CN-DBpedia%20的知识来源主要是通过爬取各种百科知识这类半结构化数据"
        self.plotter.word_cloud(text)
