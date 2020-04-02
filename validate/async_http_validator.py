import asyncio
import aiohttp
import aioredis
from aiohttp import ClientSession

timeout = aiohttp.ClientTimeout(10)

import apscheduler

async def get_proxy():
    redis = await aioredis.create_redis(('localhost', 6379))
    proxies = await redis.smembers('raw_proxy')

    return proxies


async def hello():
    async with ClientSession() as session:
        proxies = await get_proxy()
        for i in proxies:
            i = str(i, encoding='utf-8')
            proxy = "http://" + i
            async with session.get("http://httpbin.org/ip", proxy=proxy, timeout=timeout) as response:
                response = await response.read()
                print(str(response, encoding='utf-8'))


asyncio.run(hello())

# 错误处理,减分策略
