"""Base classes and functions"""
import json
from typing import Type, TypeVar
import httpx

from pyuserside.exceptions import UsersideException

AnyCategory = TypeVar("AnyCategory", bound="BaseUsersideCategory")


class BaseUsersideAPI:
    """Base API class, async-agnostic"""

    def __init__(self, url: str, key: str, category_class: Type[AnyCategory]):
        self.url = url
        self.key = key
        self.category_class = category_class

    def __getattr__(self, category):
        return self.category_class(self, category)

    def __repr__(self):
        hidden_key = "*" * len(self.key)
        result = (
            f"{self.__class__.__name__}"
            f"<url: {self.url}, "
            f"key: {hidden_key}, "
            f"category class: {self.category_class.__name__}, >"
        )
        return result

    def __str__(self):
        return f"{self.__class__.__name__}"


class BaseUsersideCategory:
    """Base category class, async-agnostic"""

    def __init__(self, api: BaseUsersideAPI, category: str):
        self.api = api
        self.category = category

    def __repr__(self):
        return f"{self.__class__.__name__}<api: {self.api}, category: {self.category}"

    def __str__(self):
        return f"{self.__class__.__name__}[{self.category}]"


def validate_response(response: httpx.Response):
    """Response status-code and decode checker"""
    try:
        content = response.json()
    except json.decoder.JSONDecodeError as exc:
        raise UsersideException("Not a valid JSON response") from exc
    if not response.status_code == 200:
        raise UsersideException(content.get("error", "No error description provided"))
    return content


def parse_response(content: dict):
    """Generic Userside response parser. Searches for id, data or list fields"""
    if (id_ := content.get("Id") or content.get("id")) is not None:
        return id_
    if (data := content.get("Data") or content.get("data")) is not None:
        return data
    if (list_ := content.get("list")) is not None:
        return list_.split(",")
    return content


def prepare_request(key: str, cat: str, action: str, **kwargs):
    """Userside request builder

    :param key: API key
    :param cat: category name
    :param action: action
    :param kwargs: parameters to be passed
    :return:
    """
    params = {"key": key, "cat": cat, "action": action}
    for field_name, field_value in kwargs.items():
        if isinstance(field_value, list):
            field_name = ",".join(field_value)
        params[field_name] = field_value
    return params
