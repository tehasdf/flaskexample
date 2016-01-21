from pytest import fixture, yield_fixture

from flaskexample import create_app
from flaskexample.models import db as _database


@fixture(scope='session')
def app():
    app = create_app(SECRET_KEY='some testing secret key')
    app.debug = True
    return app


@yield_fixture
def client(app):
    with app.test_client() as c:
        yield c


@yield_fixture
def appctx(app):
    with app.app_context():
        yield


@fixture(scope='session')
def db(request, app):
    with app.app_context():
        _database.create_all()

    @request.addfinalizer
    def _drop():
        with app.app_context():
            _database.drop_all()
