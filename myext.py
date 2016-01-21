import json
import redis


from flask import current_app



class MyRedis(object):
    def __init__(self):
        pass

    def init_app(self, app):
        if 'my_redis' in app.extensions:
            raise RuntimeError('Already initialized?')

        app.extensions['my_redis'] = {
            'conn': redis.Redis()
        }

    def publish(self, channel, data):
        data = json.dumps(data)
        if not 'my_redis' in current_app.extensions:
            raise RuntimeError('MyRedis wasnt initialized?')
        conn = current_app.extensions['my_redis']['conn']
        conn.publish(channel, data)
