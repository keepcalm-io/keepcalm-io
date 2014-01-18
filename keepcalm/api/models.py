"""
Auxiliary models for REST API
"""

import time
import redis
from django.conf import settings


class RedisStorage(object):
    """
    Redis model to manage signals
    """

    def __init__(self):
        """
        Constructor needs Redis connection params
        """

        self.connection = redis.Redis(host=settings.REDIS_HOST,
                                      port=settings.REDIS_PORT,
                                      db=0)

    def track_signal(self, user_id, signal_id, ttl, max_retries):
        """
        Registers a signal with a TTL (time to live) and a number of retries

        :param user_id: Django user id
        :type user_id: int
        :param signal_id: Django signal id
        :type signal_id: int
        :param ttl: Time to live in seconds
        :type ttl: int
        :param max_retries: Max number of retries for this signal
        :type max_retries: int

        :returns: True if everything is ok
        """

        user_id = str(user_id)
        signal_id = str(signal_id)
        signal_key = 'signal:' + user_id + ':' + signal_id
        pipe = self.connection.pipeline()
        pipe.hmset('user:' + user_id, {signal_id + ':retr': 0, signal_id + ':max_retr': max_retries})
        pipe.set(signal_key, time.time())
        pipe.expire(signal_key, ttl)
        return all(pipe.execute())

    def delete_signal(self, user_id, signal_id):
        """
        Deletes a tracked signal

        :param user_id: Django user id
        :type user_id: int
        :param signal_id: Django signal id
        :type signal_id: int

        :returns: True if everything is ok
        """

        user_id = str(user_id)
        signal_id = str(signal_id)
        pipe = self.connection.pipeline()
        pipe.hdel('user:' + user_id, signal_id + ':retr', signal_id + ':max_retr')
        pipe.delete('signal:' + user_id + ':' + 'signal_id')
        return all(pipe.execute())

    def _scan_match(self, match):
        """
        Returns all active user ids in redis

        :returns: generator
        """

        offset, items_list = self.connection.scan(match=match)
        for item in items_list:
            yield item.decode('utf-8')
        while offset:
            offset, items_list = self.connection.scan(offset, match=match)
            for item in items_list:
                yield item.decode('utf-8')

    def active_users(self, match):
        """
        Returns all active user ids in redis

        :returns: generator
        """

        yield from self._scan_match('user:')

    def active_signals(self, match):
        """
        Returns all active signal ids in redis

        :returns: generator
        """

        yield from self._scan_match('signal:')
