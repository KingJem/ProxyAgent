import asyncio
from aiohttp import ClientSession


async def hello():
    async with ClientSession() as session:
        proxy = None
        async with session.get("http://httpbin.org/ip", proxy=proxy) as response:
            response = await response.read()
            print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
