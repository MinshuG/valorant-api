import asyncio
import atexit
import json
from http.client import HTTPException
import aiohttp
import requests
from aiohttp import ClientSession
from requests import Session
import copy

from .exceptions import *


def override_params(par1, par2):
    if par2 is not None:
        par1.update(par2)
    return par1

class SyncClient:
    headers: dict = {}
    params: dict = {}
    session: Session

    def __init__(self, headers=None, params=None) -> None:
        if params is None:
            self.params = {}
        else:
            self.params = params
        if headers is None:
            self.headers = {}
        else:
            self.headers = headers
            self.session = requests.Session()

    def get(self, url: str, **kwargs) -> dict:
        response = self.session.get(url, params=override_params(copy.copy(self.params), kwargs), headers=self.headers)

        try:
            data = response.json()
        except (json.JSONDecodeError):# , simplejson.JSONDecodeError):  # linux uses simplejson??
            data = {'error': response.text}

        if response.status_code == 200:
            return data["data"]
        elif response.status_code == 400:
            raise InvalidOrMissingParameter(data["error"])
        elif response.status_code == 404:
            raise NotFound(data["error"])
        else:
            raise HTTPException(f'{data.get("error", "An error unknown occurred")}, status code {response.status_code}')


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
        asyncio.run(self.session.close())

    async def get(self, url: str, **kwargs) -> dict:
        async with self.session.get(url, params=override_params(copy.copy(self.params), kwargs), headers=self.headers) as response:
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
                raise HTTPException(
                    f'{data.get("error", "An error unknown occurred")}, status code {response.status}')
