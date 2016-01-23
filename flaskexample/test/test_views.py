# coding: utf-8

# show several testing strategies for flask views

# this uses the fixtures defined in conftest.py; you can also use the
# pytest-flask library, or flask-testing

import pytest

from werkzeug.datastructures import MultiDict
from flaskexample.views import calculate_result, BarForm
from flaskexample.models import Category


# a simple way to do TDD with flask, is to factor out the tricky/hard parts of
# code into separate functions that have nothing to do with flask, and test
# those first.
# not having to interact with flask, but rather testing simple python code,
# makes this considerably easier

# the "foo" route in views.py, extracts a number from the request data,
# passes it to a separate function which does the actual calculation,
# and then displays the result.
# this function only tests that separate function, which is "the hard part",
# in isolation
def test_calculate_view():
    assert calculate_result(5) == 120


# for when a function like this needs app context; usually it's better to
# not do this; eg. if your function needs access to app config, instead
# of using current_app, simply retrieve the config value outside of the
# function, and pass the value in
def test_creating_appctx(db, app):
    with app.app_context():
        categories = Category.query.all()


# a very direct way to test is to use flask's test client,
# using the fixtures, or eg. `with app.test_client() as c: result = c.get()`
def test_using_test_client(client):
    result = client.post('/foo', data={'n': 5})
    assert result.data == 'result is 120'


def test_bar_view(client):
    result = client.post('/bar', data={'n': 5})
    assert result.data == 'result is 120'


def test_bar_view_too_large(client):
    result = client.post('/bar', data={'n': 11})
    assert result.status_code == 400


# pytest allows creating a fixture that will make the whole test be in app context
@pytest.mark.usefixtures('appctx')
def test_bar_just_form(app):
    # this test only checks the form, which is the part of the view that should always
    # be tested
    # even if you say you don't have time for good coverage, always do test your
    # forms at least

    data = MultiDict({'n': 9})
    form = BarForm(formdata=data, csrf_enabled=False)
    assert form.validate()

    data = MultiDict({'n': 11})
    form = BarForm(formdata=data, csrf_enabled=False)
    assert not form.validate()
