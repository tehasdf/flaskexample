from flask_sqlalchemy import SQLAlchemy

from generic.models import GenericProduct
from myext import MyRedis

publisher = MyRedis()
db = SQLAlchemy()


class Category(db.Model):
    category_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=1000))


# this model contains a FK to a model from outside the application: GenericProduct
# is defined in the `generic` module, which is library code
class Product(db.Model):
    product_id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(length=1000))
    description = db.Column(db.String(length=10000))
    price = db.Column(db.Numeric())

    generic_counterpart_id = db.Column(db.Integer(), db.ForeignKey(GenericProduct.product_id))
    generic_counterpart = db.relationship(GenericProduct, uselist=False)

