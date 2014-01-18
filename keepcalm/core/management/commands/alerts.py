import os
import logging
import asyncio
import redis
from django.core.management.base import BaseCommand, CommandError
from api.models import RedisStorage

logger = logging.getLogger('alert_background_process')


class Command(BaseCommand):


    @staticmethod
    def handle_alert(redis_conn, key):
        """
        Handler to alert user for an expired task
        """

        split_key = key.split(':')
        user_id, signal_id = split_key[1], split_key[2]

        # Get actual number of retries and max retries
        retries, max_retries, ttl = redis_conn.signal_info(user_id, signal_id)

        if retries >= max_retries:
            print("Max retries exceded, take some action!")
            # TODO: payloads here (email...)
        else:
            print("Retry {}/{} for {}".format(retries + 1, max_retries, key))
            redis_conn.signal_retry(user_id, signal_id, retries + 1, ttl)


    @asyncio.coroutine
    def listener(self, redis_conn, channels):
     
        pubsub = redis_conn.connection.pubsub()
        pubsub.subscribe(channels)
        print('Listening redis...')
        for item in pubsub.listen():
            try:
                expired_key = item['data']
                if isinstance(expired_key, bytes):
                    self.handle_alert(redis_conn, expired_key.decode('utf-8'))
            except KeyError:
                continue
 
    def handle(self, *args, **options):
        r = RedisStorage()
        loop = asyncio.get_event_loop()
        asyncio.Task(self.listener(r, ['__keyevent@0__:expired']))
        loop.run_forever()
