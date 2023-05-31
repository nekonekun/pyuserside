"""
Basic methods to build request or parse response
"""
import json

import httpx

from pyuserside.exceptions import UsersideException


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
