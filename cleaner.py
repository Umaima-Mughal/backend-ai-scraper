RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def clean_books(books):
    cleaned_books = []

    for book in books:
        cleaned_books.append({
            "title": book["title"].strip(),
            "price": float(book["price"].replace("£", "")),
            "availability": book["availability"].strip(),
            "rating": RATING_MAP.get(book["rating"], 0)
        })

    return cleaned_books