from flask import Flask

from flaskexample.views import main
from flaskexample.models import db, publisher

from generic.models import db as generic_db
from generic2 import thing_views


def create_app(config=None, **kw):
    app = Flask(__name__)

    if config is not None:
        app.config.from_pyfile(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update(kw)

    db.init_app(app)
    generic_db.init_app(app)
    publisher.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(thing_views, url_prefix='/things')

    app.debug = True
    return app
