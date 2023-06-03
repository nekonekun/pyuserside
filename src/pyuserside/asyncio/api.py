"""Async Userside API client module"""
import httpx

from pyuserside.base import (
    prepare_request,
    validate_response,
    parse_response,
    BaseUsersideAPI,
    BaseUsersideCategory,
)


class UsersideAPI(BaseUsersideAPI):  # pylint: disable=too-few-public-methods
    """Userside API async client class"""

    def __init__(self, url: str, key: str, session: httpx.AsyncClient = None):
        super().__init__(url, key, AsyncUsersideCategory)
        self.session = session or httpx.AsyncClient()


class AsyncUsersideCategory(
    BaseUsersideCategory
):  # pylint: disable=too-few-public-methods
    """Generic async userside category"""

    async def _request(self, action, **kwargs):
        params = prepare_request(
            key=self.api.key, cat=self.category, action=action, **kwargs
        )
        response = await self.api.session.get(self.api.url, params=params)
        content = validate_response(response)
        return parse_response(content)

    def __getattr__(self, action):
        async def _action(**kwargs):
            return await self._request(action, **kwargs)

        return _action
