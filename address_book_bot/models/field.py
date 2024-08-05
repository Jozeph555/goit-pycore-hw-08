""" Class Field """


class Field:
    """
    Base class for record fields
    """
    def __init__(self, value):
        """
        Initializes the instance based on type of field.

        Args:
          value: The value of the field
        """
        self.value = value

    def __str__(self):
        return str(self.value)
