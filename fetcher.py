import time
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests


USER_AGENT = "backend-ai-scraper/1.0 (educational scraping project)"
REQUEST_DELAY = 1.0

_last_request_time = 0.0
_robots_cache = {}


def _wait_for_rate_limit():
    global _last_request_time

    elapsed = time.monotonic() - _last_request_time

    if elapsed < REQUEST_DELAY:
        time.sleep(REQUEST_DELAY - elapsed)


def _robots_allows(url):
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    robots_url = f"{base_url}/robots.txt"

    if base_url in _robots_cache:
        parser = _robots_cache[base_url]

        if parser is None:
            return True

        return parser.can_fetch(USER_AGENT, url)

    _wait_for_rate_limit()

    response = requests.get(
        robots_url,
        headers={"User-Agent": USER_AGENT},
        timeout=10
    )

    global _last_request_time
    _last_request_time = time.monotonic()

    if response.status_code == 404:
        _robots_cache[base_url] = None
        return True

    response.raise_for_status()

    parser = RobotFileParser()
    parser.set_url(robots_url)
    parser.parse(response.text.splitlines())

    _robots_cache[base_url] = parser

    return parser.can_fetch(USER_AGENT, url)


def fetch_page(url):
    if not _robots_allows(url):
        raise PermissionError(
            f"Scraping is disallowed by robots.txt: {url}"
        )

    _wait_for_rate_limit()

    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        timeout=10
    )

    global _last_request_time
    _last_request_time = time.monotonic()

    response.raise_for_status()
    response.encoding = "utf-8"

    return response.text