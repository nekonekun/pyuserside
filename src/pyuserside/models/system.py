"""
Category>System
https://wiki.userside.eu/API_system
"""
import datetime
from typing import Dict, Any
from pyuserside.exceptions import ParseError


class SystemInfo:  # pylint: disable=too-few-public-methods
    """Response model for get_system_info request
    https://wiki.userside.eu/API_system#get_system_info
    """

    def __init__(self, content: Dict[str, Any]):
        self.userside_version: str = content.get("userside_version")
        try:
            self.date_time_unix: datetime.datetime = datetime.datetime.fromtimestamp(
                content.get("date_time_unix")
            )
        except TypeError as exc:
            raise ParseError("SystemInfo -> date_time_unix -> invalid value") from exc
        self.date_time_string: str = content.get("date_time_string")
        self.os: str = content.get("os")  # pylint: disable=invalid-name
        self.php_version: str = content.get("php_version")

    def __repr__(self):
        result = "SystemInfo<"
        result += f"UserSide version: {self.userside_version}, "
        result += f"datetime UNIX: {self.date_time_unix.timestamp()}, "
        result += f"datetime string: {self.date_time_string}, "
        result += f"os: {self.os}, "
        result += f"PHP version: {self.php_version}"
        result += ">"
        return result
