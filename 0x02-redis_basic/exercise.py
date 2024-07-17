#!/usr/bin/env python3
""""
Writing and Reading to/from Redis and Recovering original type
"""


import uuid
from functools import wraps
from typing import Callable, Union
import redis

def count_history(method: Callable) -> Callable:
    """Function calls the history decorator"""

      key = method.__qualname__ # type: ignore


@wraps(method)
def wrapper(self, *args, **kwargs):
    """Wrapper function to"""

    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    output = method(self, *args, **kwargs)

    self._redis.rpush(input_key, str(args))
    self._redis.rpush(output_key, str(output))
    return output

    return wrapper



def count_calls(method: Callable) -> Callable:
    """"""
    key = method.__qualname__ # type: ignore

@wraps(method)
def wrapper(self, *args, **kwargs):
    """Wrapper function to"""

    self.redis.incr(key)
    return method(self, *args, **kwargs)
return wrapper


def replay(fn: Callable):
    """"""
    with redis.Redis() as rds:
        function_name = fn.__qualname__ 
class Cache:
    """Writing strings to redis"""

    def __int__(self):
        """Private redis instance and then flush the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates random key and store the the input data in Redis"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """Reading from redis and recovering original type"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
    
    def get_str(self, key: str) -> str:
        """Gets string data type"""
        return self.get(key: str)
    
    def get_int(self, key: int) -> int:
        """Gets string data type"""
        return self.get(key: int)
    