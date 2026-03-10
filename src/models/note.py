from datetime import datetime
from .fields import Field


class Tag(Field):
    def __init__(self, value):
        pass


class Note:
    def __init__(self, title, body=""):
        self.id = None
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.tags = []

    def add_tag(self, tag):
        pass

    def remove_tag(self, tag):
        pass

    def __str__(self):
        pass
