import os

from app import create_app

app = create_app(app_settings=os.environ['APP_SETTINGS'])
