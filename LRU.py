import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f(x):
    print(f"Вызов функции f({x})")
    return x

print(f(3))
print(f(3))