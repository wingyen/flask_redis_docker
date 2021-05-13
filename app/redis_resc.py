"""Sets up the redis connection and the redis queue."""

import redis



redis_cache = redis.Redis(host='redis', port=6379, db=0)

#redis_queue = Queue(connection=redis_conn)