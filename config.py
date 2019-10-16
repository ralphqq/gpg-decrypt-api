import os

from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Load env_file, if provided
ENV_FILE = os.environ.get('ENV_FILE')
if ENV_FILE is not None:
    env_path = os.path.join(BASEDIR, ENV_FILE)
    load_dotenv(env_path)


class Config:
    """Base config values."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JSONIFY_PRETTYPRINT_REGULAR = True

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = False
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
