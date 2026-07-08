from library import services, repository, utils

def handle_add():    
    title=input("Enter title of book: ")
    author=input("Enter author of book: ")
    year=(input("Enter year of book: "))
    new_book={
        'id':repository.next_id(),
        'title':title,
        'author':author,
        'year':year,
        'available':True
    }
    errors=services.validate_book(new_book)
    if errors:
        print("\nErrors in Information of new Book\n")
        for e in errors:
            print('-',e)
        return
    
    new_book['year']=int(new_book[year])
    repository.add_book(new_book)
    print("New Book Added Successfully")

def handle_list():
    for book in repository.get_all_books():
        print(utils.format_book(book))

def handle_search():
    i=1
    x=2
    while i<=3:
        user_input=input("Please Enter title/author: ")
        if not user_input.strip():
            print(f"Will ask {x} more times only. Please enter info")
        if user_input.strip():
            break
        i+=1
        x-=1

    if user_input:
        results = services.search_books(user_input.strip().lower())
        if not results:
            print("Book not found")
        else:
            for book in results:
                print(utils.format_book(book))
    else:
        print("Please type title/author first")
    

def handle_update():
    i=1
    x=2
    while i<=3:
        id_of_book=input("Enter ID of book you want to update: ")
        if not id_of_book.strip():
            print(f"Will ask {x} more times. Please Enter the info")
        if id_of_book.strip():
            break
        i+=1
        x-=1
    if id_of_book:
        if not repository.find_book(int(id_of_book)):
            print("Book not found.")
            return
        else:
            title=input('Enter title of book (changed) if not then write as it is: ')
            author=input('Enter author of book (changed) if not then write as it is: ')
            year=(input('Enter year of book (changed) if not then write as it is: '))
            available=input('Enter availability of book (changed) if not then write as it is: ').lower()=='yes'
            changes={
            'title':title,
            'author':author,
            'year':year,
            'available':available}
            errors=services.validate_book(changes)
            if errors:
                print("\nErrors in Information of Updation\n")
                for e in errors:
                    print('-',e)
                return
            else:
                changes['year']=int(changes['year'])
                if repository.update_book(id_of_book,changes):
                    print('Book Updated Successfully')
                else:
                    print("Book Id not matches!!")
    else:
        print('Please enter the id first')
        return


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
    i=1
    x=2
    while i<=3:
        id_of_book=(input('Enter id of book: '))
        if not id_of_book.strip():
            print(f"Will as {x} more times. Please enter info")
        if id_of_book.strip():
            break
        i+=1
        x-=1

    if id_of_book:
        book=repository.find_book(id_of_book)
        if not book:
            print("Book not found")
             
        else:
            repository.delete_book(id_of_book)
            print("Book Deleted Successfully")
    else:
        print('Please enter book id first')

def handle_sort():
    i=1
    x=2
    while i<=3:
        key = input("Enter (title/author): ").strip().lower()
        if not key.strip():
            print(f"Will as {x} more times. Please enter info")
        if key.strip():
            break

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
