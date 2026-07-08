from library import services, repository, utils

def handle_add():
    title=input("Enter title of book: ")
    author=input("Enter author of book: ")
    year=int(input("Enter year of book: "))
    new_book={
        'id':repository.next_id(),
        'title':title,
        'author':author,
        'year':year,
        'available':True
    }
    errors=services.validate_book(new_book)
    if errors:
        print("Errors in Information of new Book")
        return
    repository.add_book(new_book)
    print("New Book Added Successfully")

def handle_list():
    for book in repository.get_all_books():
        print(utils.format_book(book))

def handle_search():
    results = services.search_books(input("Enter title/author: "))
    if not results:
        print("Book not found")
    for book in results:
        print(utils.format_book(book))
    

def handle_update():
    id_of_book=int(input("Enter ID of book you want to update: "))
    if not repository.find_book(id_of_book):
        print("Book not found.")
        return
    title=input('Enter title of book (changed) if not then write as it is: ')
    author=input('Enter author of book (changed) if not then write as it is: ')
    year=int(input('Enter year of book (changed) if not then write as it is: '))
    available=input('Enter availability of book (changed) if not then write as it is: ').lower()=='yes'
    changes={
        'title':title,
        'author':author,
        'year':year,
        'availabile':available
    }
    repository.update_book(id_of_book,changes)
    print('Book Updated Successfully')

def handle_borrow():
    book_id = utils.prompt_int("Enter book id: ")
    book = repository.find_book(book_id)
    if not book:
        print("Book not found.")
        return
    if book["available"]:
        repository.update_book(book_id, {"available": False})
        print("Book borrowed.")
    else:
        repository.update_book(book_id, {"available": True})
        print("Book returned.")

def handle_delete():
    id_of_book=int(input('Enter id of book: '))
    book=repository.find_book(id_of_book)
    if not book:
        print("Book not found")
        return 
    repository.delete_book(id_of_book)
    print("Book Deleted Successfully")

def handle_sort():
    key = input("Enter (title/author): ").strip().lower()
    if key not in ["title","author"]:
        print("Invalid field.")
        return
    books = repository.get_all_books()
    books = services.sort_books(books, key)

    for b in books:
        print(utils.format_book(b))




def run():
    while True:
        print("\n1. Add book\n2. List all books\n3. Search Books\n4. Update Books\n5. Borrow/Return Books\n6. Delete Books\n7. Sort Books\n0. Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        match choice:
            case '1':
                handle_add()
            case '2':
                handle_list()
            case '3':
                handle_search()
            case '4':
                handle_update()
            case '5':
                handle_borrow()
            case '6':
                handle_delete()
            case '7':
                handle_sort()
            case _:
                print("Invalid Choice!!!")
