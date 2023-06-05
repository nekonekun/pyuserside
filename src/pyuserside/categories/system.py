"""
Category>System
https://wiki.userside.eu/API_system
"""
from pyuserside.base import BaseUsersideAPI, SyncUsersideCategory
from pyuserside.models.system import SystemInfo


class System(SyncUsersideCategory):  # pylint: disable=too-few-public-methods
    """System information and operation"""

    def __init__(self, api: BaseUsersideAPI):
        super().__init__(api, "system")

    def get_system_info(self):
        """get system information about Userside"""
        raw_response = self._request("get_system_info")
        response = SystemInfo.parse_obj(raw_response)
        return response
