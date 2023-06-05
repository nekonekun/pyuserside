"""Async Userside API client module"""
import httpx

from pyuserside.base import BaseUsersideAPI, AsyncUsersideCategory


class UsersideAPI(BaseUsersideAPI):  # pylint: disable=too-few-public-methods
    """Userside API async client class"""

    def __init__(self, url: str, key: str, session: httpx.AsyncClient = None):
        super().__init__(url, key, AsyncUsersideCategory)
        self.session = session or httpx.AsyncClient()
