from flask import Flask


def create_app(app_settings):
    """App factory function."""
    app = Flask(__name__)
    app.    config.from_object(app_settings)

    from app.resource import api
    api.init_app(app)

    return app

