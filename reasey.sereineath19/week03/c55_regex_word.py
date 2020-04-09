import re


def regex_word(integer, string):
    if integer <= 0:
        return '""'
    else:
        return re.sub(r'\b\w{1,' + str(integer) + r'}\b\s*', '', string)