import re

def regex_html(string):
    if len(string) == 0:
        return '""'
    return re.sub(r'(<[^>]*>)', "", string)

