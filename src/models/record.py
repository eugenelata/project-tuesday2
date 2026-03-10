from .fields import Name, Phone, Birthday, Email, Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone):
        pass

    def remove_phone(self, phone):
        pass

    def edit_phone(self, old_phone, new_phone):
        pass

    def find_phone(self, phone):
        pass

    def add_birthday(self, birthday):
        pass

    def add_email(self, email):
        pass

    def edit_email(self, new_email):
        pass

    def add_address(self, address):
        pass

    def edit_address(self, new_address):
        pass

    def __str__(self):
        pass
