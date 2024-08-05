"""Contact Handler """


from models import AddressBook, Record


def input_error(func):
    """
    Decorator function that handles ValueError
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Value Error: {e}"
        except KeyError as e:
            return f"Key Error: Contact {e} not found."
        except AttributeError:
            return "Attribute Error: Contact doesn't have the specified attribute."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner


@ input_error
def add_contact(args, book: AddressBook):
    """Adds a new contact to the 
    Addressbook"""
    name, phone, *_ = args
    if not name or not phone:
        raise ValueError("Both name and phone must be provided.")
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added"
    record.add_phone(phone)
    return message


@ input_error
def change_contact(args, book: AddressBook):
    """Changes an existing contact 
    in the Addressbook"""
    name, old_phone, new_phone, *_ = args
    if not name or not old_phone or not new_phone:
        raise ValueError("Name, old phone, and new phone must be provided.")
    record = book.find(name)
    if not record:
        raise KeyError(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact changed."


@input_error
def show_phone(args, book: AddressBook):
    """Outputs the phone numbers 
    for the specified contact"""
    name, *_ = args
    if not name:
        raise ValueError("Name must be provided.")
    record = book.find(name)
    if not record:
        raise KeyError(name)

    result = [f"Contacts for {name}:"]
    if record.phones:
        for ph in record.phones:
            ph = str(ph)
            pattern = f"({ph[:3]}){ph[3:6]}-{ph[6:8]}-{ph[8:]}"
            result.append(pattern)
    else:
        result.append("No phones")

    return "\n".join(result)


def show_all(book: AddressBook):
    """Outputs all saved contacts 
    with phone numbers"""
    if not book:
        return "Address book is empty."

    result = ["Contacts:"]
    for name, record in book.items():

        phones = []
        if record.phones:
            for ph in record.phones:
                ph = str(ph)
                pattern = f"({ph[:3]}){ph[3:6]}-{ph[6:8]}-{ph[8:]}"
                phones.append(pattern)
            phones = "; ".join(phones)
        else:
            phones = "No phones"

        result.append(f"Name: {name}, Phones: {phones}")

    return "\n".join(result)
