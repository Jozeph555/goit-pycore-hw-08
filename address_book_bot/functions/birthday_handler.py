""" Birthday Handler """


from functools import wraps
from datetime import datetime
from models import AddressBook


def input_error(func):
    """
    Decorator function that handles ValueError
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if "time data" in str(e) or "Invalid date format" in str(e):
                return "Invalid date format. Please use DD.MM.YYYY."
            elif "Birthday cannot be in the future" in str(e):
                return "Error: Birthday cannot be in the future."
            elif "Birthday year must be 1900 or later" in str(e):
                return "Error: Birthday year must be 1900 or later."
            elif "Invalid date" in str(e):
                return "Error: Invalid date. Please check the day and month values."
            else:
                return f"Value Error: {e}"
        except KeyError as e:
            return f"Contact not found: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return wrapper


@input_error
def add_birthday(args, book: AddressBook):
    """Adds a birthday to the 
    contact"""
    name, birthday, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError(name)
    try:
        datetime.strptime(birthday, "%d.%m.%Y")
    except ValueError as e:
        raise ValueError("Invalid date format. Please use DD.MM.YYYY.") from e
    record.add_birthday(birthday)
    return "Birthday added to the contact."


@input_error
def show_birthday(args, book: AddressBook):
    """Outputs the birthday 
    of the specified contact"""
    name, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError(name)
    if not record.birthday:
        return f"No birthday set for contact {name}"
    return str(record.birthday)


@input_error
def birthdays(args, book: AddressBook):
    """Show birthdays that will happen in the next week"""
    _ = args
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No birthdays in the upcoming week."
    result = "Upcoming birthdays:\n"
    for birthday in upcoming_birthdays:
        result += f"{birthday['name']}: {birthday['congratulation_date']}\n"
    return result.strip()
