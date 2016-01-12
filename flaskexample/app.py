from flask import Flask

from flaskexample.views import main
from flaskexample.models import db


def create_app(config=None):
    app = Flask(__name__)
    db.init_app(app)
    app.register_blueprint(main)
    return app
