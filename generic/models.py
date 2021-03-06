from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class GenericProduct(db.Model):
    product_id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(length=1000))
    description = db.Column(db.String(length=10000))
    price = db.Column(db.Numeric())
