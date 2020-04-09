import requests


def get_html(string):
    return requests.get(string).text
