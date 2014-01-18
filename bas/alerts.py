#!/usr/bin/env python -tt

import os
import logging
import asyncio
import redis


# Config logger
try:
    LOGFILE = os.environ['KEEPCALM_ALERTS_LOG']
except IndexError:
    LOGFILE = '/tmp/keepcalm_alerts.log'

logger = logging.getLogger('keepcalm')
handler = logging.FileHandler(LOGFILE)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
 
@asyncio.coroutine
def listener(redis_conn, channels):
 
    pubsub = redis_conn.pubsub()
    pubsub.subscribe(channels)
    logger.debug('Listening redis...')
    for item in pubsub.listen():
        print(item)
 
 
if __name__ == '__main__':
    r = redis.Redis()
    loop = asyncio.get_event_loop()
    asyncio.Task(listener(r, ['test']))
    loop.run_forever()