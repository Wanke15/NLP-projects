import logging
from flask import Blueprint


class NLPBlueprint(Blueprint):
    def __init__(self, name, import_name, init_func=None, url_prefix=None):
        self.init_func = init_func
        self.logger = logging.getLogger(__name__)
        super().__init__(name, import_name, url_prefix=url_prefix)

    def register(self, app, options, first_registration=False):
        self.logger.debug('Initialize BluePrint {}'.format(self.name))
        try:
            if self.init_func is not None:
                self.init_func()
        except Exception as e:
            self.logger.exception(
                'BluePrint {} initialization failed, Exception: {}'.format(self.name, e))
        super().register(app, options, first_registration)
