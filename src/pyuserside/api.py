"""Sync Userside API client module"""
import httpx

from pyuserside.base import prepare_request, validate_response, parse_response


class UsersideAPI:
    """Sync Userside API client class"""

    def __init__(self, url: str, key: str, session: httpx.Client = None):
        self.url = url
        self.key = key
        self.session = session or httpx.Client()

    def __getattr__(self, category):
        return UsersideCategory(self, category)


class UsersideCategory:
    """Generic userside category"""

    def __init__(self, api: UsersideAPI, category: str):
        self.api = api
        self.category = category

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
