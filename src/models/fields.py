from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        # TODO: validate that value is exactly 10 digits
        pass


class Birthday(Field):
    def __init__(self, value):
        # TODO: parse value string in DD.MM.YYYY format to date
        pass


class Email(Field):
    def __init__(self, value):
        # TODO: validate email format (regex: user@domain.tld)
        pass


class Address(Field):
    def __init__(self, value):
        # TODO: store the address value
        pass
