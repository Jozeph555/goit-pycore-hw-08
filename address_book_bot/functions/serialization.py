""" Module for serialization"""


import pickle
from models import AddressBook


def save_data(book, filename="addressbook.pkl"):
    """
    Saves the AddressBook state.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    """
    Creates an empty AddressBook or loads 
    restored state of AddressBook.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
