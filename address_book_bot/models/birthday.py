""" Class Birthday """


from datetime import datetime, date
from .field import Field


class Birthday(Field):
    """
    A class for storing user's birthday
    """
    def __init__(self, value):
        """
        Initializes the user's birthday field.

        Args:
          value: User's birthday
        
        Raises:
          ValueError if date format isn't DD.MM.YYYY, or if the 
          date is invalid (e.g., in the future or before 1900)
        """
        super().__init__(value)
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y").date()
            self.validate_date(birthday)
            self.value = birthday
        except ValueError as e:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from e


    def validate_date(self, birthday):
        """
        Checks if the date is not in the future and not earlier than 1900.
        """
        today = date.today()
        if birthday > today:
            raise ValueError("Birthday cannot be in the future")
        if birthday.year < 1900:
            raise ValueError("Birthday year must be 1900 or later")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
