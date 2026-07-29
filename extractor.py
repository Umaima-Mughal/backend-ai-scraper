def extract_books(soup):
    books = []

    articles = soup.find_all("article", class_="product_pod")

    for book in articles:
        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating = book.p["class"][1]

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    return books