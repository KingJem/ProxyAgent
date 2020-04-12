import asyncio

import aiohttp
from aiohttp import ClientSession
from fake_useragent import UserAgent

from settings import VALIDATOR_TIMEOUT
from utils.utils import random_target_web

timeout = aiohttp.ClientTimeout(VALIDATOR_TIMEOUT)

header = {"User-Agent": UserAgent().random}


async def get_ip_port(**kwargs):
    pass


async def verify_proxy(**kwargs):
    async with ClientSession() as session:
        try:
            async with session.get(url=random_target_web, timeout=VALIDATOR_TIMEOUT, header=header) as response:
                if response.statuscode == 200:
                    # 爬虫入库操作
                    pass


        except asyncio.TimeoutError:
            # 删除爬虫操作
            pass
        except Exception as e:
            pass


async def main():


if __name__ == '__main__':
    asyncio.run(verify_proxy())

# 从爬虫那边获取代理
#
