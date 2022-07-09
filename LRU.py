import asyncio
from functools import wraps
from datetime import timedelta

def cache(key_function: Callable, ttl: timedelta):
    def _decorator(function):
        @wraps(function)
        async def _function(*args, **kwargs):
            cache_key = key_function(*args, **kwargs)
            result = await _cache.get(cache_key)
            if result:
                return result
            result = await function(*args, **kwargs)
            asyncio.create_task(_cache.set(cache_key, result, ttl=ttl.total_seconds()))
            return result
        return _function
    return _decorator


def _key_function(user, account_id):
    return f"user-account-{user.id}-{account_id}"


@cache(_key_function, timedelta(hours=3))
async def get_user_account(*, user: User, account_id: int):
    ...