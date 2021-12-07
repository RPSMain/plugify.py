"""
Apache-2.0

Copyright 2021 RPS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the LICENSE file for the specific language governing permissions and
limitations under the License.
"""
import asyncio
import aiohttp
import json
from typing import Any, Optional, Type, TracebackType, TYPE_CHECKING, TypeVar, Coroutine, Union, Dict
from urllib.parse import quote as uriquote

if TYPE_CHECKING:
    from .types.snowflake import Snowflake, SnowflakeList # Hopefully snowflakes are implemented before public release
    from types import TracebackType

    T = TypeVar('T')
    BE = TypeVar('BE', bound=BaseException)
    MU = TypeVar('MU', bound='MaybeUnlock')
    Response = Coroutine[Any, Any, T]

version = "2"

async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding='utf-8')
    try:
        if response.headers['content-type'] == 'application/json':
            return json.loads(text)
    except KeyError:
        pass

    return text

class Route:
    BASE = f"https://api.plugify.cf/v{version}" # https://docs.plugify.cf/http/#http-overview

    def __init__(self, method, route, **parameters: Any):
        self.method = method
        self.path = route.format(**parameters)
        url = self.BASE + self.path
        if parameters:
            url = url.format_map({k: uriquote(v) if isinstance(v, str) else v for k, v in parameters.items()})
        self.url: str = url

        # Used for bucket cooldowns
        self.channel_id = parameters.get("channel_id")
        self.group_id = parameters.get("group_id")

    @property
    def bucket(self):
        """The Route's bucket identifier."""
        return f"{self.channel_id}:{self.group_id}:{self.path}"

# Based Of discord.py's implementation
class MaybeUnlock:
    def __init__(self, lock: asyncio.Lock) -> None:
        self.lock: asyncio.Lock = lock
        self._unlock: bool = True

    def __enter__(self: MU) -> MU:
        return self

    def defer(self) -> None:
        self._unlock = False

    def __exit__(
        self,
        exc_type: Optional[Type[BE]],
        exc: Optional[BE],
        traceback: Optional[TracebackType],
    ) -> None:
        if self._unlock:
            self.lock.release()

class HTTPClient:
    """HTTPClient for connecting to Plugify"""
    pass

class RatelimitClient:
    """Handles Ratelimiting To Prevent 429s"""
    pass
