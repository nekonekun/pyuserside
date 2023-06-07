"""Userside API sync client module"""
import httpx
from pyuserside.base import BaseUsersideAPI, SyncUsersideCategory
from pyuserside.categories.system import System
from pyuserside.categories.notepad import Notepad
from pyuserside.categories.commutation import Commutation


class UsersideAPI(BaseUsersideAPI):  # pylint: disable=too-few-public-methods
    """Userside API client class"""

    def __init__(self, url: str, key: str, session: httpx.Client = None):
        super().__init__(url, key, SyncUsersideCategory)
        self.session = session or httpx.Client()
        self.system = System(self)
        self.notepad = Notepad(self)
        self.commutation = Commutation(self)
