from flask import Blueprint, render_template

from generic.models import GenericProduct
from flaskexample.models import Product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.join(GenericProduct).all()
    return render_template("index.html", products=products)
