# coding: utf-8
"""Example showing how to use flask-sqlalchemy models without app context,
with vanilla sqlalchemy orm.

"""


from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from flaskexample.models import Product, db

# prepare using sqlalchemy as usual...
eng = create_engine('postgresql+psycopg2:///asdf')
sess = Session()

# Now just make sure flask-sqla's metadata is bound to your engine, and you're done.
db.metadata.bind = eng

# this query will now succeed...
print sess.query(Product).all()

# but this will fail; this is flask-sqla's approach, and for this, you still need
# app context
try:
    Product.query.all()
except RuntimeError:
    pass
