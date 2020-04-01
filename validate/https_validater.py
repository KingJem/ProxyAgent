import asyncio
import functools
from concurrent.futures.thread import ThreadPoolExecutor
from requests_html import HTMLSession
import sys
session = HTMLSession()


async def get_response(executor, *, url, loop: asyncio.AbstractEventLoop = None, ):
    if not loop:
        loop = asyncio.get_running_loop()
    request = functools.partial(session.get, url)
    return loop.run_in_executor(executor, request)


async def bulk_requests(executor, *,
                        urls,
                        loop: asyncio.AbstractEventLoop = None, ):
    for url in urls:
        yield await get_response(executor, url=url, loop=loop)


def filter_unsuccesful_requests(responses_and_exceptions):
    return filter(
        lambda url_and_response: not isinstance(url_and_response[1], Exception),
        responses_and_exceptions.items()
    )


async def main():
    executor = ThreadPoolExecutor(10)
    urls = [
        "https://baidu.com",
        "https://cnblogs.com",
        "https://163.com",
    ]
    requests = [request async for request in bulk_requests(executor, urls=urls, )]
    responses_and_exceptions = dict(zip(urls, await asyncio.gather(*requests, return_exceptions=True)))
    responses = {url: resp.html for (url, resp) in filter_unsuccesful_requests(responses_and_exceptions)}

    for res in responses.items():
        print(res[1].xpath("//head//title//text()")[0])

    for url in urls:
        if url not in responses:
            print(f"No successful request could be made to {url}. Reason: {responses_and_exceptions[url]}",
                  file=sys.stderr)


asyncio.run(main())