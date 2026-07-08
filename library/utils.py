import datetime

def write_log(message: str) -> None:
 """Append a timestamped line to app.log."""
 with open("app.log","a") as file:
        file.write(f"{datetime.datetime.now() -  {message}}\n")


def prompt_int(message: str) -> int:
 """Ask until the user types a valid integer."""
 while True:
    message=input('Enter a value: ')
    if message.isdigit():
       return int(message)
    print('Please enter a valid number')


def format_book(book: dict) -> str:
 """Return a single, aligned display row for a book."""
 return f"ID: {book['id']:<4} Title: {book['title']:<20} Author: {book['author']:<20} Year: {book['year']:<4}   Availability: {book['available']}"