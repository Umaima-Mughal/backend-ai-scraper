from urllib.parse import urljoin

from saver import save_books
from fetcher import fetch_page
from parser import parse_html
from extractor import extract_books
from cleaner import clean_books


START_URL = "https://books.toscrape.com/"
MAX_PAGES = 2


def scrape_pages(start_url, max_pages=None):
    current_url = start_url
    all_books = []
    pages_scraped = 0

    while current_url and (max_pages is None or pages_scraped < max_pages):
        print(f"Scraping: {current_url}")

        html = fetch_page(current_url)

        soup = parse_html(html)

        books = extract_books(soup)

        cleaned_books = clean_books(books)

        all_books.extend(cleaned_books)

        pages_scraped += 1

        next_link = soup.select_one("li.next a")

        if next_link:
            current_url = urljoin(current_url, next_link["href"])
        else:
            current_url = None

    return all_books, pages_scraped


if __name__ == "__main__":
    books, pages_scraped = scrape_pages(
        START_URL,
        MAX_PAGES
    )

    save_books(books)

    print(f"Pages scraped: {pages_scraped}")
    print(f"Books collected: {len(books)}")
    print("Books saved successfully!")