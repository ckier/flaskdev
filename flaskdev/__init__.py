# Copyright 2016 Molecular Devices, LLC
# All Rights Reserved.

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    log_file = app.config.get('LOG_FILE')
    if log_file:
        handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=3)
    else:
        handler = logging.StreamHandler()
    log_level = app.config.get('LOG_LEVEL', logging.INFO)
    log_format = app.config.get('LOG_FORMAT')
    handler.setLevel(log_level)
    handler.setFormatter(log_format)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')
    app.logger.info('Application starting.')
    return app
