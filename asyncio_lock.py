import asyncio

from asyncio import Lock

cache = {}
lock = Lock()

async def get_stuff(url):
    '''
    get_stuff 被多处调用
    :param url:
    :return:
    '''
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff('g.cn')
    # do something parse


async def use_stuff():
    stuff = await get_stuff()
