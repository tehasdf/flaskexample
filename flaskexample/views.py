# coding: utf-8

# this is a plain and simple views module, structured using a blueprint
# for more info on blueprints, see http://flask.pocoo.org/docs/dev/blueprints/

import json

from flask import Blueprint, render_template, request, render_template_string, abort

from wtforms import IntegerField
from wtforms.validators import NumberRange

from flask_wtf import Form

from generic.models import GenericProduct
from flaskexample.models import Product, publisher
from myext import simple


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # note that this uses both the Product, and the GenericProduct, defined
    # using separate db.Models; all that was needed was to simply init_app the
    # generic db, which allowed declaring a FK to the library model
    products = Product.query.join(GenericProduct).all()
    return render_template("index.html", products=products)



# some simple POST handlers; also see their tests in flaskexample/test/test_views.py
def calculate_result(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


@main.route('/foo', methods=['POST'])
def foo():
    n = int(request.form['n'])
    result = calculate_result(n)
    return (render_template_string("result is {{ result }}", result=result),
        200, {'Content-Type': 'text/plain'})


class BarForm(Form):
    n = IntegerField(validators=[NumberRange(max=10)])


@main.route('/bar', methods=['POST'])
def bar():
    form = BarForm(csrf_enabled=False)

    if form.validate_on_submit():
        n = form.data['n']
        result = calculate_result(n)
        return (render_template_string("result is {{ result }}", result=result),
            200, {'Content-Type': 'text/plain'})
    else:
        abort(400)


# route using the redis extension from myext.py
@main.route('/publish')
def publish():
    publisher.publish('channel', {'some': 'data'})
    return ('ok, published', 200, {'Content-Type': 'text/plain'})


# route using the simple extension from myext.py
@main.route('/simple')
def show_simple():
    return render_template_string('simple is {{ simple }}', simple=simple)
