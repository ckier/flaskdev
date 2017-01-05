# Copyright 2016 Molecular Devices, LLC
# All Rights Reserved.

from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config_by_name[config_name])
    # db.init_app(app)
    # login_manager.init_app(app)
    # moment.init_app(app)
    # toolbar.init_app(app)
    #
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')
    return app
