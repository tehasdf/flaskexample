from flask import Flask

from flaskexample.views import main


def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
