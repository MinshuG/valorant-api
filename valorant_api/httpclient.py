import requests
from aiohttp import ClientSession
import aiohttp
import json
import atexit
import asyncio

from .exceptions import *


class SyncClient:
    headers: dict = {}
    params: dict = {}

    def __init__(self, headers=None, params=None) -> None:
        if params is None:
            self.params = {}
        else:
            self.params = params
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers

    def get(self, url: str):
        response = requests.get(url, params=self.params, headers=self.headers)

        try:
            data = response.json()
        except json.JSONDecodeError:
            data = {'error': response.text}

        if response.status_code == 200:
            return data["data"]
        elif response.status_code == 400:
            raise InvalidOrMissingParameter(data["error"])
        elif response.status_code == 404:
            raise NotFound(data["error"])
        else:
            raise Exception(f'{data.get("error", "An error unknown occurred")}, status code {response.status_code}')


class AsyncClient:
    headers: dict = {}
    params: dict = {}
    session: ClientSession

    def __init__(self, headers=None, params=None) -> None:
        if params is None:
            self.params = {}
        else:
            self.params = params
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers
        self.session = aiohttp.ClientSession()
        atexit.register(self.close)

    def close(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.session.close())

    async def get(self, url: str):
        # async with aiohttp.ClientSession() as session:
        async with self.session.get(url, params=self.params, headers=self.headers) as response:
            try:
                data = await response.json()
            except aiohttp.ContentTypeError:
                data = {'error': response.text}

            if response.status == 200:
                return data["data"]
            elif response.status == 400:
                raise InvalidOrMissingParameter(data["error"])
            elif response.status == 404:
                raise NotFound(data["error"])
            else:
                raise Exception(
                    f'{data.get("error", "An error unknown occurred")}, status code {response.status}')
