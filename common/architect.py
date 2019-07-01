from abc import ABC, abstractmethod


class MLPipeline(ABC):
    def __init__(self, pre_processor, predictor, post_processor):
        if pre_processor is not None:
            self.pre_processor = pre_processor
        else:
            self.pre_processor = None
        if predictor is not None:
            self.predictor = predictor
        else:
            self.detector = None
        if post_processor is not None:
            self.post_processor = post_processor
        else:
            self.post_processor = None

    @abstractmethod
    def process(self):
        pass