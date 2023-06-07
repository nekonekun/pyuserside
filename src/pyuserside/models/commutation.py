"""
Category>Commutation
https://wiki.userside.eu/API_commutation
"""
from typing import Dict, Any, List
from pyuserside.exceptions import UsersideException


class Link:
    """
    Part of response model for get_data request
    https://wiki.userside.eu/API_commutation#get_data
    """

    def __init__(self, content: Dict[str, Any]):
        self.comment = content.get("comment")
        self.connect_id = content.get("connect_id")
        self.direction = content.get("direction")
        self.interface = content.get("interface")
        self.object_id = content.get("object_id")
        self.object_type = content.get("object_type")

    def __getitem__(self, item: str):
        return getattr(self, item)

    def __repr__(self):
        result = "Link<"
        result += f"comment: {self.comment}, "
        result += f"connect_id: {self.connect_id}, "
        result += f"direction: {self.direction}, "
        result += f"interface: {self.interface}, "
        result += f"object_id: {self.object_id}, "
        result += f"object_type: {self.object_type}"
        result += ">"
        return result

    def __eq__(self, other):
        return self.connect_id == other.connect_id


class PortCommutationWithFinish:
    """
    Part of response model for get_data request
    https://wiki.userside.eu/API_commutation#get_data
    """

    def __init__(self, results: Dict[int | str, Link]):
        self.dataset: Dict[int, Link] = {
            int(port): link for port, link in results.items() if isinstance(port, int)
        }
        self.finish = results.get("finish")

    def __getitem__(self, item):
        if item == "finish":
            return self.finish
        if not isinstance(item, int):
            try:
                item = int(item)
            except ValueError as exc:
                raise UsersideException(f"{item} is not valid int-like") from exc
        return self.dataset.get(item)

    def __iter__(self):
        return iter(self.dataset.values())

    def __len__(self):
        return len(self.dataset.values())

    def __repr__(self):
        return f"PortLinks[total {len(self)}]"

    @classmethod
    def from_dict(cls, obj):
        """Get PortCommutationWithFinish object from dict"""
        if not isinstance(obj, dict):
            real_type = type(obj)
            raise ValueError(
                f"from_dict argument must be dict, got {real_type} instead"
            )
        results = {}
        for port, link in obj.items():
            if port.isdigit():
                results[int(port)] = Link(link)
            else:
                results["finish"] = Link(link)
        return cls(results)


class CommutationSet:
    """
    Response model for get_data request
    https://wiki.userside.eu/API_commutation#get_data
    """

    def __init__(self, results: Dict[int, List[Link]]):
        self.dataset: Dict[int, List[Link]] = results

    def __getitem__(self, item):
        if not isinstance(item, int):
            try:
                item = int(item)
            except ValueError as exc:
                raise UsersideException(f"{item} is not valid int-like") from exc
        return self.dataset.get(item)

    def __iter__(self):
        return iter(self.dataset.values())

    def __len__(self):
        return len(self.dataset.values())

    def __repr__(self):
        return f"Links[total {len(self)}]"

    @classmethod
    def from_dict(cls, obj):
        """Get CommutationSet object from dict"""
        if not isinstance(obj, dict):
            real_type = type(obj)
            raise ValueError(
                f"from_dict argument must be dict, got {real_type} instead"
            )
        results = {}
        for port, commutation_list in obj.items():
            results[int(port)] = [Link(link) for link in commutation_list]
        return cls(results)


class CommutationSetWithFinish:
    """
    Response model for get_data request
    https://wiki.userside.eu/API_commutation#get_data
    """

    def __init__(self, results: Dict[int, PortCommutationWithFinish]):
        self.dataset: Dict[int, PortCommutationWithFinish] = results

    def __getitem__(self, item):
        if not isinstance(item, int):
            try:
                item = int(item)
            except ValueError as exc:
                raise UsersideException(f"{item} is not valid int-like") from exc
        return self.dataset.get(item)

    def __iter__(self):
        return iter(self.dataset.values())

    def __len__(self):
        return len(self.dataset.values())

    def __repr__(self):
        return f"Links[total {len(self)}]"

    @classmethod
    def from_dict(cls, obj):
        """Get CommutationSet object from dict"""
        if not isinstance(obj, dict):
            real_type = type(obj)
            raise ValueError(
                f"from_dict argument must be dict, got {real_type} instead"
            )
        results = {}
        for port, commutation_dict in obj.items():
            results[int(port)] = PortCommutationWithFinish.from_dict(commutation_dict)
        return cls(results)
