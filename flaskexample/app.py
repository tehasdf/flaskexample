# coding: utf-8

"""The main entry point module containing the application factory
"""

# for more info on application factories, see
# http://flask.pocoo.org/docs/dev/patterns/appfactories/

from flask import Flask


# flask applications often have trouble with circular imports, which leads them
# to putting imports like these on the bottom of the file, or inside functions

# the most common cause of that is importing your app object into your views
# module. This is a bad thing; instead, you should use flask.current_app
# at runtime (in app context, eg. inside your view functions, when serving a
# request), and use the extension pattern at config time.

# this example doesn't even have a module-level app object that you could
# have imported into your views module; instead, it only exposes an app factory
from flaskexample.views import main
from flaskexample.models import db, publisher


# the following imports are libraries that are not parts of the app:

# a generic reusable module containing db models. It is not part of the app,
# it might be a library that you installed using pip
from generic.models import db as generic_db

# another generic/reusable module, containing a flask blueprint. Reusable
# blueprints are unfortunately somewhat rare, but conceptually they should be
# similar to reusable django apps
from generic2 import thing_views

# library exposing a simple flask extension
from myext import setup_simple


def create_app(config=None, **kw):
    app = Flask(__name__)

    # apply some defaults etc. to the config here
    app.debug = True
    if config is not None:
        app.config.from_pyfile(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.update(kw)

    # build the app by mounting extensions & blueprints on it
    # some are part of this app, some are generic
    db.init_app(app)
    generic_db.init_app(app)
    publisher.init_app(app)
    setup_simple(app)

    app.register_blueprint(main)
    app.register_blueprint(thing_views, url_prefix='/things')
    return app
