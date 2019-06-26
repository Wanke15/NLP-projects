#!/usr/bin/env python3


class NLPException(Exception):
    status_code = 500


class RunTimeException(NLPException):
    pass


class ConfigurationError(NLPException):
    pass


class TimeoutException(NLPException):
    status_code = 408


class InvalidInputException(NLPException):
    status_code = 400
    pass


class UnauthorizedError(NLPException):
    status_code = 401
