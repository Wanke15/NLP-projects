import traceback

from apis.nlpblueprint import NLPBlueprint
from apis.nlpresponse import NLPResponse
from apis import nlpexception


def init():
    pass


nlp_bp = NLPBlueprint('main', __name__, init)


@nlp_bp.app_errorhandler(nlpexception.RunTimeException)
def handle_runtime_exception(error):
    nlp_bp.logger.error("Run Time Error: {}".format(error))
    return NLPResponse(str(error), error.status_code, False)


@nlp_bp.app_errorhandler(nlpexception.ConfigurationError)
def handle_runtime_exception(error):
    nlp_bp.logger.error("Configuration Error: {}".format(error))
    return NLPResponse(str(error), error.status_code, False)


@nlp_bp.app_errorhandler(nlpexception.InvalidInputException)
def handle_invalid_input(error):
    nlp_bp.logger.error("Invalid Input Error: {}".format(error))
    return NLPResponse(str(error), error.status_code, False)


@nlp_bp.app_errorhandler(nlpexception.TimeoutException)
def handle_timeout(error):
    nlp_bp.logger.error("Timeout: {}".format(error))
    return NLPResponse(str(error), error.status_code, False)


@nlp_bp.app_errorhandler(nlpexception.UnauthorizedError)
def handle_timeout(error):
    nlp_bp.logger.error("Unauthorized request: {}".format(error))
    return NLPResponse(str(error), error.status_code, False)


@nlp_bp.app_errorhandler(Exception)
def handle_unexpected_exception(error):
    nlp_bp.logger.error("Unexpected exception: {}".format(error))
    nlp_bp.logger.error(traceback.format_exc())
    return NLPResponse(str(error), 500, False)


@nlp_bp.route('/nlp/v1/health', methods=['GET'])
def health_check():
    return "I'm doing great"

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
