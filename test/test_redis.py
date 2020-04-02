import redis

host = '127.0.0.1'
port = 6379

r = redis.Redis(host=host, db=15, decode_responses=True, port=port)
r.hset('site', 'redis', 'redis.com')

print(r.hget('site', 'redis'))
