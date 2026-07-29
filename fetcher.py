import requests


def fetch_page(url):
    response = requests.get(url)

    response.encoding = "utf-8"

    return response.text