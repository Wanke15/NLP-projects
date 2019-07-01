from common.post_processing import SentimentPostprocessor
from common.preprocessing import SentimentPreprocessor
from common.architect import MLPipeline
from sentiment_analysis.model import SentimentModel


class SentimentPipeline(MLPipeline):
    instance = None

    def __init__(self, pre_processor=None, predictor=None, post_processor=None):
        super().__init__(pre_processor=pre_processor, predictor=predictor, post_processor=post_processor)

    def process(self, sentence):
        if not isinstance(sentence, list):
            raw_sentence = [sentence]
            result = [sentence]
        else:
            raw_sentence = sentence
            result = sentence
        if self.pre_processor is not None:
            result = self.pre_processor(result)
        if self.predictor is not None:
            result = self.predictor(result)
        if self.post_processor is not None:
            result = self.post_processor(raw_sentence, result)
        return result

    @classmethod
    def init(cls, count_vec_path, classifier_path, stop_words_path):
        sentiment_preprocessor = SentimentPreprocessor(stop_words_path)
        sentiment_model = SentimentModel(count_vec_path, classifier_path)
        sentiment_postprocessor = SentimentPostprocessor()

        cls.instance = SentimentPipeline(pre_processor=sentiment_preprocessor.preprocess,
                                         predictor=sentiment_model.process,
                                         post_processor=sentiment_postprocessor.post_process)

    @classmethod
    def predict(cls, sentence):
        result = cls.instance.process(sentence)
        return result
