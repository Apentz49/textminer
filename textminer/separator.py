import re

def words(input):
    words = re.findall(r"\b[\d]*[A-Za-z-]+", input)
    if words:
        return words
    else:
        return None

def phone_number(input):
    pass

def money(input):
    pass

def zipcode(input):
    pass

def date(input):
    pass