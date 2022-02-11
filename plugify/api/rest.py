"""
MIT License

Copyright (c) 2021-present VincentRPS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import json
import logging
from typing import TYPE_CHECKING, Any, Dict, Union

import aiohttp

if TYPE_CHECKING:

    from ..types.snowflake import (  # Hopefully snowflakes are implemented before public release
        Snowflake,
        SnowflakeList,
    )

_log = logging.getLogger(__name__)

async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding="utf-8")
    try:
        if response.headers["content-type"] == "application/json":
            return json.loads(text)
    except KeyError:
        pass

    return text


class HTTPClient:
    """HTTPClient for connecting to Plugify

    .. versionadded:: 1.0.0
    """

    def __init__(
        self,
        app_id: str,
        app_secret: str,
    ):
        self._url = "https://api.plugify.cf/v2"
        self.headers = {}
        self.app_id = app_id
        self.app_secret = app_secret
        
    async def request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ):
        self._session = aiohttp.ClientSession()

        if 'json' in kwargs:
            kwargs['data'] = json.dumps(kwargs.pop('json'))
        
        if 'token' in kwargs:
            self.headers['Authorization'] = kwargs.pop('token')
        
        kwargs['headers'] = self.headers
        
        async with self._session.request(method=method, url=self.url+endpoint, **kwargs) as r:

            data = await json_or_text(response=r)

            if r.status == 429:
                # currently impossible due to the state of the api
                ...
            
            elif r.status == 200:
                _log.debug('> %s', data)
                return data
            
            else:
                _log.error('> %s', data)


    def get_app(self):
        return self.request('GET', f'/apps/info/{self.app_id}')
    
    def create_app(self, name: str):
        json = {
            'name': name
        }
        return self.request('POST', '/apps/create', json=json)
    
    def login_app(self):
        json = {
            'id': self.app_id,
            'secret': self.app_secret
        }
        r = self.request('POST', '/app/login', json=json)
        self.token = r['token']
        return r
    
    def verify_app(self):
        json = {
            'id': self.app_id,
            'token': self.token,
            'accept': True,  # this is not a bool?
            'recaptchaToken': ''  # uh what is mean't to be here?
        }
        return self.request('POST', '/apps/login/verify', json=json)
    
    def create_channel(
        self,
        name: str,

    ):
        ...