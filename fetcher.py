import requests


def fetch_page(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "EducationalScraper/1.0"
        },
        timeout=10
    )

    response.raise_for_status()

    return response.text