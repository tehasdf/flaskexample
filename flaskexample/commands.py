import os.path

from click import group, command
from flask.cli import script_info_option, FlaskGroup, with_appcontext


from flaskexample.app import create_app
from flaskexample.models import db, Product

from generic.models import db as generic_db


def prepare_app(info):
    config = info.data.get('config')
    if config:
        config = os.path.join('..', config)

    return create_app(config)


@group(cls=FlaskGroup, create_app=prepare_app)
@script_info_option('--config', script_info_key='config')
def cli(**params):
    pass


@cli.command('createdb')
@with_appcontext
def createdb():
    db.create_all()
    generic_db.create_all()

@cli.command('product')
@with_appcontext
def create_product():
    name = raw_input('name?')
    new_product = Product(name=name)
    db.session.add(new_product)
    db.session.commit()
