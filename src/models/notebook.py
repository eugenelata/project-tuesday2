from collections import UserDict


class NoteBook(UserDict):
    def __init__(self):
        super().__init__()
        self._next_id = 1

    def add_note(self, note):
        pass

    def find_by_id(self, note_id):
        pass

    def search(self, query):
        pass

    def edit_note(self, note_id, new_title=None, new_body=None):
        pass

    def delete(self, note_id):
        pass

    def find_by_tag(self, tag):
        pass

    def sort_by_tags(self):
        pass
