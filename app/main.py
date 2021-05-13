from flask import Flask
from .redis_resc import redis_cache
import redis
import requests


app = Flask(__name__)


def get_hit_count():
    retries = 5
    while True:
        try:
            hits = redis_cache.incr('hits')
            redis_cache.expire('hits', 60)
            return hits
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello_world():
    count = get_hit_count()

    return 'Hello World! I have been seen {} times.\n'.format(count)


def sub_random_joke():
    pass