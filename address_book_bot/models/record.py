""" Class Record """


from .name import Name
from .phone import Phone
from .birthday import Birthday


class Record:
    """
    A class for storing information about a contact, 
    including name and phone list.
    """
    def __init__(self, name):
        """
        Initializes the instance based on record.

        Args:
          name: The contact name.
        """
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        """
        Adds phone number to the record.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """
        Removes specific phone number from the record.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        """
        Replaces old phone number with new phone number
        in the record.
        """
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break
        else:
            raise ValueError("Phone number not found")

    def find_phone(self, phone):
        """
        Finds specific phone number in the record.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        """
        Adds birthday to the record.
        """
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value},\
            \nbirthday: {self.birthday.value},\
            \nphones: {'; '.join(p.value for p in self.phones)}"
