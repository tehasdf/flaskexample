from flask import Blueprint, render_template

from flaskexample.models import Product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)
