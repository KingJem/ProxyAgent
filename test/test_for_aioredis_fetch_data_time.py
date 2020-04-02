import asyncio
import time

import aioredis

loop = asyncio.get_event_loop()


async def run():
    redis = await aioredis.create_redis(('localhost', 6379))
    val = await redis.smembers('raw_proxy')
    print(val)
    redis.close()
    await redis.wait_closed()


loop.run_until_complete(run())
