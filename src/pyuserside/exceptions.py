"""Userside exceptions collection"""


class UsersideException(BaseException):
    """Most generic exception"""


class ParseError(UsersideException):
    """Parsing error"""
