from saver import save_books
from fetcher import fetch_page
from parser import parse_html
from extractor import extract_books
from cleaner import clean_books

if __name__ == "__main__":
    url = "https://books.toscrape.com/"

    html = fetch_page(url)

    soup = parse_html(html)

    books = extract_books(soup)

    cleaned_books = clean_books(books)

    save_books(cleaned_books)

    print("Books saved successfully!")