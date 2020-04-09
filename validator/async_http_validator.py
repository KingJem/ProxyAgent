import asyncio
import time

import aiohttp
import aioredis
from aiohttp import ClientSession

timeout = aiohttp.ClientTimeout(10)
start = time.time()

async def get_proxy():
    redis = await aioredis.create_redis(('localhost', 6379))
    proxies = await redis.smembers('raw_proxy')

    return proxies


async def verify_proxy():
    async with ClientSession() as session:
        proxies = await get_proxy()
        for i in proxies:
            i = str(i, encoding='utf-8')
            proxy = "http://" + i
            try:
                async with session.get("http://httpbin.org/ip", proxy=proxy, timeout=timeout) as response:
                    response = await response.read()
                    # print(str(response, encoding='utf-8'))
            except asyncio.TimeoutError:
                pass
            except Exception as e:
                pass

if __name__ == '__main__':

    asyncio.run(verify_proxy())
    end = time.time()
    total_time = end-start
    print(total_time)

# 错误处理,减分策略

