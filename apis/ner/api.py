import os
import logging

from flask import request, render_template


from apis.nlpblueprint import NLPBlueprint
from apis.nlpexception import InvalidInputException
from utils import get_base_dir

from ner.ner_parse import NER
from ner.render import render_entities_content

logger = logging.getLogger(__name__)


def init_ner():
    NER.init(os.path.join(get_base_dir(), 'resources/models/ner/spacy_model'))


def init():
    logger.info('NLP named entity recognition API initializing...')
    init_ner()


api_bp = NLPBlueprint('ner', __name__, init, url_prefix='/nlp/v1/ner')


@api_bp.route("/dashboard", methods=["GET", "POST"])
def ner_dashboard():
    if request.method == 'GET':
        text = """
        Asian shares skidded on Tuesday after a rout in tech stocks put Wall Street to the sword.
        """
    elif request.method == 'POST':
        text = request.form.get('text_area')
    else:
        return InvalidInputException("No text provided to draw word cloud!")
    ents = NER.get_ner(text)
    try:
        ents_markup = render_entities_content(text, ents)
        return render_template('ner.html', text=text, entities_content=ents_markup)
    except Exception as e:
        print(e)
        return "Render error!"