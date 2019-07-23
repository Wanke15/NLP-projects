from collections import Counter
import os
import uuid

import jieba
from pyecharts.charts import WordCloud

from utils import get_base_dir


class WordCloudVis:
    def __init__(self):
        jieba.lcut("你好")
        self.base_dir = get_base_dir()
        with open(os.path.join(self.base_dir, 'resources/data/中英文停用词.txt'), 'r', encoding='utf8') as f:
            self.stopwords = [l.strip() for l in f.readlines()]

    def word_cloud(self, text):
        all_words = [word.lower() for word in jieba.cut(text, cut_all=False) if word not in self.stopwords and len(word) > 1]
        counter = Counter(all_words)

        wordcloud = WordCloud()
        wordcloud.add("", counter.items(), word_size_range=[10, 80], shape='diamond')
        _name = uuid.uuid4()
        wordcloud.render(os.path.join(self.base_dir, 'templates/vis/word_cloud/{}.html'.format(_name)))
        return _name
