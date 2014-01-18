#!/usr/bin/env python -tt

import os
import logging
import asyncio
import redis


# Config logger
try:
    LOGFILE = os.environ['KEEPCALM_ALERTS_LOG']
except KeyError:
    LOGFILE = '/tmp/keepcalm_alerts.log'

logger = logging.getLogger('keepcalm')
handler = logging.FileHandler(LOGFILE)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def handle_alert(key):
    """
    Handler to alert user for an expired task
    """

    # TODO: handle if key expired is valid 
    print("Expired {}".format(key))
 

@asyncio.coroutine
def listener(redis_conn, channels):
 
    pubsub = redis_conn.pubsub()
    pubsub.subscribe(channels)
    logger.debug('Listening redis...')
    for item in pubsub.listen():
        try:
            expired_key = item['data']
            if isinstance(expired_key, bytes):
                handle_alert(expired_key.decode('utf-8'))
                logger.debug(item)
        except KeyError:
            continue
 
 
if __name__ == '__main__':
    r = redis.Redis()
    loop = asyncio.get_event_loop()
    asyncio.Task(listener(r, ['__keyevent@0__:expired']))
    loop.run_forever()
