from flask import Flask

from config import Config


def create_app(app_settings):
    """App factory function."""
    app = Flask(__name__)
    app.config.from_object(app_settings)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app

