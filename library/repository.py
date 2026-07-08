from library import storage, models

def get_all_books() -> list[dict]:
 """Read + parse every book."""
 return [models.parse_line(line) for line in storage.read_all_lines()]

def add_book(book: dict) -> None:
 """Serialize and append one book."""
 storage.append_line(models.to_line(book))


def find_book(book_id: int) -> dict | None:
 """Return the matching book, or None."""
 for book in get_all_books():
        if book["id"] == book_id:
            return book

def update_book(book_id: int, changes: dict) -> bool:
 """Apply changes to one book; rewrite the file. Return success."""
 books = get_all_books()
 for book in books:
    if book["id"] == book_id:
        book.update(changes)
        storage.write_all_lines([models.to_line(b) for b in books])
        return True
    return False
 
def delete_book(book_id: int) -> bool:
 """Remove one book; rewrite the file. Return success."""
 books = get_all_books()
 new_books = [b for b in books if b["id"] != book_id]
 if len(new_books) == len(books):
    return False
 storage.write_all_lines([models.to_line(b) for b in new_books])
 return True

def next_id() -> int:
 """Compute the next auto-increment id."""
 books = get_all_books()
 if not books:
    return 1
 return max(b["id"] for b in books) + 1
