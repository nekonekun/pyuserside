"""
Category>System
https://wiki.userside.eu/API_system
"""
import datetime
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class SystemInfo(BaseModel):  # pylint: disable=too-few-public-methods
    """Response model for get_system_info request
    https://wiki.userside.eu/API_system#get_system_info
    """

    userside_version: str
    date_time_unix: datetime.datetime
    date_time_string: str
    os: str
    php_version: str
