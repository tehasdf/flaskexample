from flask import Blueprint, jsonify

from generic2.models import Thing, db

thing_views = Blueprint('things', __name__)


@thing_views.record
def prepare(state):
    app = state.app
    db.init_app(app)
    with app.app_context():
        db.create_all()


@thing_views.route('/')
def index():
    things = Thing.query.all()
    return jsonify(things=[thing.to_json() for thing in things])
