# coding: utf-8

"""Flask extension for publishing to redis
"""

# This is a simple extension that needs to hold a redis connection
# Usage should be similar to that of flask-sqlalchemy:
#  - instantiate the extension somewhere in your code, `r = MyRedis()`
#  - mount it on your app, `r.init_app(app)`, typically in your app factory
#  - in app context (eg. inside your view functions), use the methods on the
#    extension instance, eg. `r.publish('foo', {'bar': 'baz'})`

# The main point of flask extensions, or the "flask extension pattern",
# is that you keep all the state on your app object. This is done by passing
# the actual app into the init_app setup method, and later in runtime, using
# current_app instead

import json
import redis

from werkzeug.local import LocalProxy
from flask import current_app


class MyRedis(object):
    def init_app(self, app):
        if 'my_redis' in app.extensions:
            raise RuntimeError('Already initialized?')

        # put some extension-specific state on the app object;
        # note that no state at all is stored on this instance
        app.extensions['my_redis'] = {
            'conn': redis.Redis()
        }

    def publish(self, channel, data):
        # this method will be called at runtime, eg. from view functions
        data = json.dumps(data)
        if not 'my_redis' in current_app.extensions:
            raise RuntimeError('MyRedis wasnt initialized?')

        # retrieve the state from current_app; this is the same state we prepared
        # in init_app
        conn = current_app.extensions['my_redis']['conn']

        conn.publish(channel, data)

# usage:
# creates the extension instance in flaskexample/models.py
# setup in flaskexample/app.py
# publishing in flaskexample/views.py, the publish route



# this pattern can be simplified using werkzeug's LocalProxy:

# the init_app setup method: again, keeps no state, puts the data on the app instad
def setup_simple(app):
    app.extensions['simple'] = 42


# the function for use at runtime: retrieves the state from current_app
def _get_simple():
    return current_app.extensions['simple']

# now in your views, you can do `_get_simple()`
# we can skip the function call by using LocalProxy,
# allowing us to just use `simple` instead:
simple = LocalProxy(_get_simple)

# example usage: setup in flaskexample/app.py, usage in flaskexample/views.py,
# the show_simple route
