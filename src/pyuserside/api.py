"""Userside API sync client module"""
import httpx
from pyuserside.base import (
    prepare_request,
    validate_response,
    parse_response,
    BaseUsersideAPI,
    BaseUsersideCategory,
)


class UsersideAPI(BaseUsersideAPI):  # pylint: disable=too-few-public-methods
    """Userside API client class"""

    def __init__(self, url: str, key: str, session: httpx.Client = None):
        super().__init__(url, key, SyncUsersideCategory)
        self.session = session or httpx.Client()


class SyncUsersideCategory(
    BaseUsersideCategory
):  # pylint: disable=too-few-public-methods
    """Generic sync userside category"""

    def _request(self, action, **kwargs):
        params = prepare_request(
            key=self.api.key, cat=self.category, action=action, **kwargs
        )
        response = self.api.session.get(self.api.url, params=params)
        content = validate_response(response)
        return parse_response(content)

    def __getattr__(self, action):
        def _action(**kwargs):
            return self._request(action, **kwargs)

        return _action
