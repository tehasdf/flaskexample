# one easy way to deploy an application like this, is to create a wsgi.py file
# or similar, that will actually construct the app providing config values

# now your wsgi server, like eg. uwsgi, can run the application imported from
# this module, eg.
# `uwsgi --http :8000 -w wsgi:application`

# if your config is much more involved than this, and for big apps it
# often will be, you might want to put this preparation code in a python package,
# and write a setup.py for it. This way you'll be able to install it into your virtualenv.

from flaskexample import create_app

application = create_app(config='config')
