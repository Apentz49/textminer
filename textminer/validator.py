import re

def binary(thing):
    return re.match(r"[01]+", thing)

def binary_even(thing):
    return re.match(r"[01]+0$", thing)

def hex(thing):
    return re.match(r"[A-fa-f0-9]+$", thing)
    # This is not passing,


def word(thing):
    return re.match(r"\A[\d]*[A-Za-z-]+\Z", thing)
    # \A = Start of string ignore m flag, \Z End ignore m flag
    # Not sure exactly what they do other then work

def words():
    pass

def phone_number(thing):
    return re.search(r"\(?(\d{3})\)?[\-\.]?\s*(\d{3})[\-\.]?(\d{4})", thing)

def money():
    pass

def zipcode(thing):
    return re.match(r"^\d{5}(-\d{4})?$", thing)

def date():
    pass
