import spacy


class NER:
    instance = None

    @classmethod
    def init(cls, model_name):
        cls.instance = spacy.load(model_name)

    @classmethod
    def get_ner(cls, text):
        doc = cls.instance(text)
        ents = []
        for ent in doc.ents:
            ents.append({'type': ent.label_, 'startIndex': ent.start_char, 'endIndex': ent.end_char})
        res = {'entities': ents}
        return res
