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
import collections

class _Hold:
    def __init__(self):
        self._storage = collections.OrderedDict()
    
    async def cache(self, hold: str, data: dict):
        self._storage[hold] = data
    
    async def get(self, hold: str):
        self._storage.get(hold)
    
    async def pop(self, hold: str):
        self._storage.pop(hold)

class Cache:
    """Represents normally cached objects"""
    def __init__(self, **custom_impl):
        self.members = custom_impl.get("members") or _Hold()
        self.groups = custom_impl.get("groups") or _Hold()
        self.messages = custom_impl.get("messages") or _Hold()
        self.channels = custom_impl.get("channels") or _Hold()

class ConnectionState:
    def __init__(self, **customs):
        self.cache = customs.get("cache") or Cache()
