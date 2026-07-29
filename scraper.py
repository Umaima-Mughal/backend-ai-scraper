from fetcher import fetch_page
from parser import parse_html
from extractor import extract_books


if __name__ == "__main__":
    url = "https://books.toscrape.com/"

    html = fetch_page(url)

    soup = parse_html(html)

    books = extract_books(soup)

    for book in books[:5]:
        print(book)