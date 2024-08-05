"""Class AddressBook"""


from typing import List, Dict
from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    """
    A class for storing and managing records.
    """

    def add_record(self, record):
        """
        Adds the record to the address book.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Finds the record by the name.
        """
        return self.data.get(name)

    def delete(self, name):
        """
        Removes the record from address 
        book by the name.
        """
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self) -> List[Dict[str, str]]:
        """
        Returns a list of users whose birthday is 7 days ahead including the current day.

        Returns:
        list[dict]: List of dictionary where each dictionary contains user's name
        and congratulation date in format "%Y.%m.%d".
        """

        current_date = datetime.today().date()

        def get_congratulation_date(birthday: datetime.date) -> datetime.date:
            """ 
            Determines the congratulation date based on the birthday.
            If the birthday falls on a weekend, it moves the congratulation to the next Monday.
            """
            if birthday.weekday() >= 5:  # Saturday or Sunday
                #Calculates how many days will be added to get Monday
                days_to_monday = 7 - birthday.weekday()
                return birthday + timedelta(days=days_to_monday)
            return birthday

        greeting_list = []
        for record in self.data.values():
            try:
                birthdate = datetime.strptime(str(record.birthday), "%d.%m.%Y").date()
                birthdate_this_year = birthdate.replace(year=current_date.year)
                days_until_birthday = (birthdate_this_year - current_date).days

                if days_until_birthday >= 0 and days_until_birthday <= 7:
                    greeting_dict = {
                        "name": record.name.value,
                        "congratulation_date": get_congratulation_date(birthdate_this_year)\
                            .strftime("%d.%m.%Y")
                    }
                    greeting_list.append(greeting_dict)
            except (AttributeError, ValueError):
                # Skip records without a birthday or with invalid date format
                continue

        return greeting_list
