#!/usr/bin/env python3

import logging
from importlib import import_module

from flask import Flask

from apis.app import nlp_bp
from apis.utils import get_config


def create_app():
    logger = logging.getLogger(__name__)

    app = Flask('NLP Services')

    app.register_blueprint(nlp_bp)  # main blue print

    config = get_config()
    services = config.get('services')
    # services = ['basic']
    for service in services:
        try:
            service_module_name = "apis.{}.api".format(service)
            service_module = import_module(service_module_name)
            api_bp = getattr(service_module, "api_bp")
        except Exception as e:
            logger.exception("Failed to load API {}!".format(service))
            logger.error(e)
        else:
            app.register_blueprint(api_bp)
    logger.info("NLP projects application started")
    return app
