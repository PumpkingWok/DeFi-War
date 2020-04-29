import requests


def append_params(url, *args):
    if len(args) > 0:
        url += '?' + args[0]
    for param in args[1:]:
        url += '&' + param
    return url


def execute_request(url):
    r = requests.get(url=url)
    data = r.json()
    return data
