from click import group, command
from flask.cli import script_info_option, FlaskGroup, with_appcontext


from flaskexample.app import create_app
from flaskexample.models import db


@group(cls=FlaskGroup, create_app=create_app)
@script_info_option('-config', script_info_key='config')
def cli(**params):
    pass


@cli.command('chuj')
@with_appcontext
def createdb():
