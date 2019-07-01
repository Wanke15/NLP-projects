import logging
import os
import codecs
import json
from json import JSONDecodeError

import yaml

from flask import request
from werkzeug import http

from apis.nlpexception import InvalidInputException

logger = logging.getLogger(__name__)


def get_base_dir():
    # the base dir is "../.."
    return os.path.dirname(os.path.dirname(__file__))


_config = None


def get_config(path=None):
    global _config
    if _config is not None:
        # already loaded config
        return _config

    _config = {}
    logger.debug('Loading configuration...')

    if path is None:
        path = os.path.join(get_base_dir(), 'apis', 'config.yaml')

    _config = load_config(path)
    return _config


def load_config(path):
    if os.path.exists(path):
        return load_yaml(path)
    else:
        logger.error("Config file {} does not exist".format(path))
    return {}


def load_yaml(path):
    with open(path, encoding="utf-8") as fin:
        return yaml.safe_load(fin)


def validate_content_type():
    if 'Content-Type' not in request.headers:
        raise InvalidInputException("Expects Content-Type to be application/json")
    content_type = http.parse_options_header(request.headers['Content-Type'])[0]
    if content_type != 'application/json':
        raise InvalidInputException("Expects Content-Type to be application/json")


def get_body():
    validate_content_type()
    try:
        if request.data[:3] == codecs.BOM_UTF8:
            logger.debug("Request data include UTF8 BOM")
            return json.loads(request.data.decode("utf-8-sig"))
        else:
            return json.loads(request.data.decode("utf-8"))

    except JSONDecodeError:
        raise InvalidInputException("Request body is not in valid JSON format")