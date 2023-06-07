"""
Category>Notepad
https://wiki.userside.eu/API_notepad
"""
import datetime
from typing import Dict, Any
from pyuserside.exceptions import UsersideException, ParseError


class FieldDescription:  # pylint: disable=too-few-public-methods
    """
    Part of response model for get_chapter request
    https://wiki.userside.eu/API_notepad#get_chapter
    """

    def __init__(self, content: Dict[str, Any]):
        try:
            self.id: int = int(content.get("id"))  # pylint: disable=invalid-name
        except ValueError as exc:
            raise ParseError("FieldDescription -> id -> invalid value") from exc
        self.name: str = content.get("name")

    def __repr__(self):
        result = "Field<"
        result += f"id: {self.id}, "
        result += f"name: {self.name}"
        result += ">"
        return result


class FieldDescriptionSet:
    """
    Part of response model for get_chapter request
    https://wiki.userside.eu/API_notepad#get_chapter
    """

    def __init__(self, results: Dict[int, FieldDescription]):
        self.dataset: Dict[int, FieldDescription] = results

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
        return f"Fields[total {len(self)}]"

    @classmethod
    def from_dict(cls, obj):
        """Get FieldDescriptionSet object from dict"""
        if not isinstance(obj, dict):
            real_type = type(obj)
            raise ValueError(
                f"from_dict argument must be dict, got {real_type} instead"
            )
        return cls({int(k): FieldDescription(v) for k, v in obj.items()})


class Chapter:  # pylint: disable=too-few-public-methods
    """
    Part of response model for get_chapter request
    https://wiki.userside.eu/API_notepad#get_chapter
    """

    def __init__(self, content: Dict[str, Any]):
        try:
            self.id: int = int(content.get("id"))  # pylint: disable=invalid-name
        except ValueError as exc:
            raise ParseError("Chapter -> id -> invalid value") from exc
        self.name: str = content.get("name")
        fields = content.get("fields")
        if not fields:
            fields = {}
        self.fields = FieldDescriptionSet.from_dict(fields)

    def __repr__(self):
        result = "Chapter<"
        result += f"id: {self.id}, "
        result += f"name: {self.name}, "
        result += f"fields: [{len(self.fields)}]"
        result += ">"
        return result

    def __getitem__(self, item):
        return getattr(self, item)


class ChapterSet:
    """
    Response model for get_chapter request
    https://wiki.userside.eu/API_notepad#get_chapter
    """

    def __init__(self, results: Dict[int, Chapter]):
        self.dataset: Dict[int, Chapter] = results

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
        return f"Chapters[total {len(self)}]"

    @classmethod
    def from_dict(cls, obj):
        """Get ChapterSet object from dict"""
        if not isinstance(obj, dict):
            real_type = type(obj)
            raise ValueError(
                f"from_dict argument must be dict, got {real_type} instead"
            )
        return cls({int(k): Chapter(v) for k, v in obj.items()})


class Field:  # pylint: disable=too-few-public-methods
    """
    Part of response model for get_note request
    https://wiki.userside.eu/API_notepad#get_note
    """

    def __init__(
        self, id: int, value: str  # pylint: disable=invalid-name,redefined-builtin
    ):
        self.id = id  # pylint: disable=invalid-name
        self.value = value

    def __repr__(self):
        result = "Field<"
        result += f"id: {self.id}, "
        result += f"value: {self.value}"
        result += ">"
        return result


class FieldSet:  # pylint: disable=too-few-public-methods
    """
    Part of response model for get_note request
    https://wiki.userside.eu/API_notepad#get_note
    """

    def __init__(self, results: Dict):
        self.dataset = {}
        for (
            id,  # pylint: disable=invalid-name,redefined-builtin
            value,
        ) in results.items():
            try:
                id: int = int(id)  # pylint: disable=invalid-name
            except ValueError as exc:
                raise ParseError("Field -> id -> invalid value") from exc
            field = Field(id=id, value=value)
            self.dataset[id] = field

    def __getitem__(self, item):
        if not isinstance(item, int):
            try:
                item = int(item)
            except ValueError as exc:
                raise UsersideException(f"{item} is not valid int-like") from exc
        return self.dataset.get(item).value

    def __len__(self):
        return len(self.dataset.values())

    def __iter__(self):
        return iter(self.dataset.values())

    def __repr__(self):
        return f"Fields[total {len(self)}]"


class Note:  # pylint: disable=too-few-public-methods
    """
    Part of response model for get_note request
    https://wiki.userside.eu/API_notepad#get_note
    """

    def __init__(self, content: Dict[str, Any]):
        try:
            self.id: int = int(content.get("id"))  # pylint: disable=invalid-name
        except ValueError as exc:
            raise ParseError("Note -> id -> invalid value") from exc
        try:
            self.chapter_id: int = int(content.get("chapter_id"))
        except ValueError as exc:
            raise ParseError("Note -> chapter_id -> invalid value") from exc
        try:
            self.date_edit: datetime.datetime = datetime.datetime.strptime(
                content.get("date_edit"), "%Y-%m-%d %H:%M:%S"
            )
        except (ValueError, TypeError) as exc:
            raise ParseError("Note -> date_edit -> invalid value") from exc
        self.fields: FieldSet = FieldSet(content.get("fields"))

    def __repr__(self):
        result = "Note<"
        result += f"id: {self.id}, "
        result += f"chapter id: {self.chapter_id}, "
        result += f"date edit: {self.date_edit.isoformat()}, "
        result += f"fields: [{len(self.fields)}]"
        result += ">"
        return result

    def __getitem__(self, item: str):
        return getattr(self, item)


class NoteSet:
    """
    Response model for get_note request
    https://wiki.userside.eu/API_notepad#get_note
    """

    def __init__(self, results: Dict[int, Note]):
        self.dataset: Dict[int, Note] = results

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
        return f"Notes[total {len(self)}]"

    @classmethod
    def from_dict(cls, obj):
        """Get NoteSet object from dict"""
        if not isinstance(obj, dict):
            real_type = type(obj)
            raise ValueError(
                f"from_dict argument must be dict, got {real_type} instead"
            )
        return cls({int(k): Note(v) for k, v in obj.items()})
