import os
DATA_FILE: str = os.path.join("data", "books.txt")
DELIMITER: str = "|"
FIELDS: list[str] = ["id", "title", "author", "year", "available"]