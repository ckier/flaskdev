# Copyright 2016 Molecular Devices, LLC
# All Rights Reserved.

import logging


class Config:
    DEBUG = False
    RELOAD = False

    # Set LOG_FILE to empty string to use console handler
    LOG_FILE = 'flaskdev.log'
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestingConfig(Config):
    TESTING = True
    # Needed if using flask-wtf (forms)
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    pass

config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
