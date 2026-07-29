from fetcher import fetch_page
from parser import parse_html


if __name__ == "__main__":
    url = "https://books.toscrape.com/"

    html = fetch_page(url)

    soup = parse_html(html)

    print(soup.title.text.strip())