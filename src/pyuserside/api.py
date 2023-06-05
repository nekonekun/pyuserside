"""Userside API sync client module"""
import httpx
from pyuserside.base import BaseUsersideAPI, SyncUsersideCategory


class UsersideAPI(BaseUsersideAPI):  # pylint: disable=too-few-public-methods
    """Userside API client class"""

    def __init__(self, url: str, key: str, session: httpx.Client = None):
        super().__init__(url, key, SyncUsersideCategory)
        self.session = session or httpx.Client()
