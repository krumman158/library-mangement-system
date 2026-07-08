Why this Project?

A I have finished the fundamentals: variables, strings, numbers, Booleans, conditionals, loops, data
structures (lists, dicts, comprehensions, generators, lambda, unpacking), functions, and file handling.
Individually, you can use all of these. The one thing a fundamentals course can't teach in isolated files is
how to organize them so a program stays readable as it grows.
That's the whole point of this project. You are not learning new syntax so much as learning where code
belongs. We'll build a Library Management System where you can add books, list them, search,
borrow/return, update, and delete — with all data living in a text file.
There is deliberately no UI and no database. Just Python, the standard library, and a .txt file. 

Key Concept:-

In Chapter 8 I have learned four types of functions. This project simply gives each type its own file:
● Action functions (do something, e.g. touch a file) → live in storage.py
● Transformation functions (raw data in, structured data out) → live in models.py
● Validation functions (return True/False or a list of errors) → live in services.py
● Orchestrator functions (call the others in the right order) → live in cli.py

Folder Structure:-

library-management-system/
├── README.md # what it is, how to run
├── requirements.txt # empty for now — teaches the convention
├── .gitignore # ignore __pycache__/, data/*.txt if you like
├── main.py # entry point — thin, ~3 lines
│
├── data/
│ └── books.txt # the file your CRUD operates on
│
├── library/ # the application package
│ ├── __init__.py # marks this folder as a package (can be empty)
│ ├── config.py # constants: file path, delimiter, field names
│ ├── models.py # record <-> line (transformation functions)
│ ├── storage.py # low-level file read/write (action functions)
│ ├── repository.py # CRUD over records, built on storage + models
│ ├── services.py # validation, search, sort (business logic)
│ ├── cli.py # the menu + all input()/print() (orchestrator)
│ └── utils.py # logging (write_log!), input helpers, formatting
│
└── tests/ # stretch goal — simple test scripts
 └── test_smoke.py


What Each File does:-

File              Responsibility                 Function type                   Must NOT do

config.py         Constants only:                   -                           Contain logic   
                  DATA_FILE, DELIMITER,
                  FIELDS. No functions.                                       

models.py         parse_line() and to_line()      Transformation              Touch files or ask for input.
                  convert a text line
                  to/from a book dict. 
                    
storage.py        Read/write raw lines to           Action                    Know what a book is
                  books.txt.Knows nothing 
                  about “books”. 
                
repository.py     CRUD in terms of records: add,    Orchestrator (data)         Print or read input
                  get all, find,update, delete. 

services.py       Validate a book, search, filter,   Validation +                 Do file I/O directly
                  sort. The business rules.          Transformation

cli.py            The menu loop, every input() and    Orchestrator (app)          Read/write the file
                  print(). Calls services.                                        directly.

utils.py          write_log(), prompt_int(),          Mixed helpers               Hold business rules
                  formatting a row for display. 
                
main.py           Start the app.                      Entry point                  Contain any logic


The menu
==== Library Management System ====
1. Add book
2. List all books
3. Search books
4. Update book
5. Borrow / Return book
6. Delete book
0. Exit

                   

                  
 

