import re


def regex_urls(string):
    if len(string) < 0:
        return '""'
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|\[!*\(\),]|(?:%[0-9a-fA-F]))+', \
        string)
    return urls

#print(regex_urls("search engine: http://www.google.com"))
