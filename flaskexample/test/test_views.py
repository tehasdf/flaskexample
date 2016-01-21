import pytest

from werkzeug.datastructures import MultiDict
from flaskexample.views import calculate_result, BarForm
from flaskexample.models import Category


def test_calculate_view():
    assert calculate_result(5) == 120


def test_using_test_client(client):
    result = client.post('/foo', data={'n': 5})
    assert result.data == 'result is 120'


def test_creating_appctx(db, app):
    with app.app_context():
        categories = Category.query.all()


def test_bar_view(client):
    result = client.post('/bar', data={'n': 5})
    assert result.data == 'result is 120'


def test_bar_view_too_large(client):
    result = client.post('/bar', data={'n': 11})
    assert result.status_code == 400


@pytest.mark.usefixtures('appctx')
def test_bar_just_form(app):
    data = MultiDict({'n': 9})
    form = BarForm(formdata=data, csrf_enabled=False)
    assert form.validate()

    data = MultiDict({'n': 11})
    form = BarForm(formdata=data, csrf_enabled=False)
    assert not form.validate()
