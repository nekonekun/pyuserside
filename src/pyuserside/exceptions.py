"""Userside exceptions collection"""


class UsersideException(BaseException):
    """Most generic exception"""


class ParseError(UsersideException):
    """Parsing error"""


class InvalidRequestParametersError(UsersideException):
    """Invalid parameter error"""
