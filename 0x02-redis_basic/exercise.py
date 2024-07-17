#!/usr/bin/env python3
""""
Writing and Reading to/from Redis and Recovering original type
"""


import uuid
from typing import Union
import redis


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
