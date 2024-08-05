""" Class Phone """


from .field import Field


class Phone(Field):
    """
    A class for storing a phone number.
    """
    def __init__(self, value):
        """
        Initializes the phone number field.

        Args:
          value: The phone number
        
        Raises:
          ValueError if phone number doesn't have 10 digits
        """
        if not self.validate(value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

    def validate(self, phone):
        """
        Validates if phone number has 10 digits.
        """
        return phone.isdigit() and len(phone) == 10
