"""
plugify.py
~~~~~~~~~~
Pythonic API Wrapper For https://plugify.cf

:copyright: 2021-present VincentRPS
:license: MIT
"""

__title__ = "plugify"
__author__ = "VincentRPS"
__license__ = "MIT"
__copyright__ = "Copyright 2021 RPS"
__version__ = "1.0.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import Literal, NamedTuple

from .client import *
from .dispatch import *
from .enums import *
from .api import *
from .group import *
from .user import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0, minor=1, micro=0, releaselevel="candidate", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())
