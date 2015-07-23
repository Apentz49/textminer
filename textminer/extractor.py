import re

def phone_numbers(text):
    return re.findall(r"[(]?\d{3}[-.)]?[ ]?\d{3}[-.]?\d{4}", text)


def emails(text):
    return re.findall(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\."
                      r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9]"
                      r"(?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]"
                      r"(?:[a-z0-9-]*[a-z0-9])?", text)