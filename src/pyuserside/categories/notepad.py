"""
Category>Notepad
https://wiki.userside.eu/API_notepad
"""
from pyuserside.base import SyncUsersideCategory, BaseUsersideAPI
from pyuserside.models.notepad import ChapterSet, NoteSet


class Notepad(SyncUsersideCategory):
    """Notepad"""

    def __init__(self, api: BaseUsersideAPI):
        super().__init__(api, "notepad")

    def get_chapter(self):
        """Information about notepad chapters"""
        raw_response = self._request("get_chapter")
        response = ChapterSet.from_dict(raw_response)
        return response

    def get_note(
        self,
        id: int | str = None,  # pylint: disable=invalid-name,redefined-builtin
        chapter_id: int | str = None,
    ) -> NoteSet:
        """Information about notes"""
        raw_response = self._request("get_note", id=id, chapter_id=chapter_id)
        response = NoteSet.from_dict(raw_response)
        return response
