import json


def save_books(books, filename="data/books.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            books,
            file,
            indent=4,
            ensure_ascii=False
        )