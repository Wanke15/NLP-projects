import unittest

from ner.ner_parse import NER
from ner.render import render_entities_content


class TestNER(unittest.TestCase):
    def setUp(self):
        NER.init('en_core_web_sm')

    def test_ner_parse(self):
        text = 'Asian shares skidded on Tuesday after a rout in tech stocks put Wall Street to the sword'
        print(NER.get_ner(text))

    def test_markup(self):
        text = 'Asian shares skidded on Tuesday after a rout in tech stocks put Wall Street to the sword'
        res = NER.get_ner(text)
        print(render_entities_content(text, res))
