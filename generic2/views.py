# coding: utf-8

# this module exports a blueprint with some views; that it uses a database,
# is an implementation detail of the blueprint, and we don't want the app code
# to worry about initializing the db; so, use the @record function to
# allow the blueprint itself to initialize the db, when registered

from flask import Blueprint, jsonify

from generic2.models import Thing, db

thing_views = Blueprint('things', __name__)


# use record_once to only make it run once in case the app registers this
# blueprint multiple times (eg. under several url prefixes)
@thing_views.record_once
def prepare(state):
    app = state.app
    # use app.config here if needed
    db.init_app(app)
    with app.app_context():
        db.create_all()


@thing_views.route('/')
def index():
    things = Thing.query.all()
    return jsonify(things=[thing.to_json() for thing in things])
