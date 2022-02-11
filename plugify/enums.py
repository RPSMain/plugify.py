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


class Enum:
    def __new__(cls, name, value):
        setattr(cls, name, value)


# should this be needed?
class APIErrors(Enum):
    """Class Defines Error Enums: https://docs.plugify.cf/http/#apierror"""

    UNKNOWN = 0
    MISSING_TOKEN = 1
    INCORRECT_TOKEN = 2
    INVALID_DATA = 3
    INVALID_CAPTCHA_RESPONSE = 4
    INVALID_EMAIL = 5
    EMAIL_USED = 6
    USERNAME_CLAIMED = 7
    NO_SUCH_USER = 8
    NO_SUCH_GROUP = 9
    INCORRECT_PASSWORD = 10
    NOT_VERIFIED = 11
    INVALID_VERIFICATION_TOKEN = 12
    NO_SUCH_INVITE = 13
    NOT_ENOUGH_PERMS = 14
    NO_INVITE_CODE = 15
    INVALID_USERNAME = 16
    ALREADY_IN_GROUP = 17
    NO_SUCH_APP = 18
    INVALID_SECRET = 19
    NO_SUCH_CHANNEL = 20
    NO_SUCH_MEMBER = 21
    USER_NOT_BANNED = 22
