from library import repository

def validate_book(book: dict) -> list[str]:
 """Return a list of error messages (empty list means valid)."""
 error_lst=[]
 if not book['title'].strip():
  error_lst.append('Title is required')
 if not isinstance(book['year'],int) and len(book['year'])!=4:
  error_lst.append("Year must be int and must be of 4 digits")
 if not book['author'].strip():
  error_lst.append('Author is required')
 return error_lst

   
def search_books(query: str) -> list[dict]:
 """Case-insensitive match on title or author."""
 query=query.lower()
 return [
    book for book in repository.get_all_books()
    if query in book["title"].lower() or query in book["author"].lower() 
    ]

def sort_books(books: list[dict], key: str = "title") -> list[dict]:
 """Return books sorted by the given field..."""
 return sorted(books,key=lambda b:b[key])

