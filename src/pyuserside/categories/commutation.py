"""
Category>Commutation
https://wiki.userside.eu/API_commutation
"""
from pyuserside.base import BaseUsersideAPI, SyncUsersideCategory
from pyuserside.exceptions import InvalidRequestParametersError
from pyuserside.models.commutation import CommutationSet, CommutationSetWithFinish


VALID_GET_DATA_OBJECT_TYPES = [
    "customer",
    "switch",
    "radio",
    "cross",
    "fiber",
    "splitter",
]


class Commutation(SyncUsersideCategory):
    """Objects commutation"""

    def __init__(self, api: BaseUsersideAPI):
        super().__init__(api, "commutation")

    def add(  # pylint: disable=too-many-arguments
        self,
        object_type: str,
        object_id: str,
        object1_side: str,
        object1_port: str,
        object2_type: str,
        object2_id: str,
        object2_side: str,
        object2_port: str,
    ):
        """objects commutation"""
        raw_response = self._request(
            "add",
            object_type=object_type,
            object_id=object_id,
            object1_side=object1_side,
            object1_port=object1_port,
            object2_type=object2_type,
            object2_id=object2_id,
            object2_side=object2_side,
            object2_port=object2_port,
        )
        return raw_response

    def delete(self, object_type: str, object_id: str, object_port: str):
        """erase commutation"""
        raw_response = self._request(
            "delete",
            object_type=object_type,
            object_id=object_id,
            object_port=object_port,
        )
        return raw_response

    def get_data(
        self,
        object_type: str,
        object_id: str | int,
        is_finish_data: int | str | bool = False,
    ):
        """get commutation array"""
        if object_type not in VALID_GET_DATA_OBJECT_TYPES:
            valid_object_types_string = ", ".join(VALID_GET_DATA_OBJECT_TYPES)
            raise InvalidRequestParametersError(
                f"object_type must be one of [{valid_object_types_string}]"
            )
        try:
            is_finish_data = int(is_finish_data)
        except ValueError as exc:
            raise InvalidRequestParametersError(
                "is_finish_data must be bool or 0/1"
            ) from exc
        if is_finish_data not in [0, 1]:
            raise InvalidRequestParametersError("is_finish_data must be bool or 0/1")
        raw_response = self._request(
            "get_data",
            object_type=object_type,
            object_id=object_id,
            is_finish_data=is_finish_data,
        )
        if is_finish_data:
            response = CommutationSetWithFinish.from_dict(raw_response)
        else:
            response = CommutationSet.from_dict(raw_response)
        return response
