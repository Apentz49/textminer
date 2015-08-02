import re

def binary(thing):
    return re.match(r"[01]+", thing)

def binary_even(thing):
    return re.match(r"[01]+0$", thing)

def hex(thing):
    match = re.match(r"^[A-Fa-f0-9]+$", thing)

    if match:
        return True
    else:
        return False

def word(thing):
    return re.match(r"\A[\d]*[A-Za-z-]+\Z", thing)
    # \A = Start of string ignore m flag, \Z End ignore m flag
    # Not sure exactly what they do other then work

def words(thing):
    pass

def phone_number(thing):
    return re.search(r"\(?(\d{3})\)?[\-\.]?\s*(\d{3})[\-\.]?(\d{4})", thing)

def money(thing):
    match = re.match(r"\$", thing)
    if match:
        return True
    else:
        return False

def zipcode(thing):
    return re.match(r"^\d{5}(-\d{4})?$", thing)

def date():
    pass
