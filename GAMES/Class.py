import queue

# Initialize library data using dictionaries
library = [
    {
        "title": "Book1",
        "author": "Author1",
        "genre": "Fiction",
        "ISBN": "123456789",
        "availability": True,
    },
    {
        "title": "Book2",
        "author": "Author2",
        "genre": "Non-Fiction",
        "ISBN": "987654321",
        "availability": True,
    },
]

# Initialize empty queues for book reservations
reservation_queues = {}


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    isbn = input("Enter ISBN: ")
    availability = True

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "ISBN": isbn,
        "availability": availability,
    }

    library.append(book)
    print("Book added successfully.")


def remove_book():
    isbn = input("Enter ISBN of the book to remove: ")
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            print("Book removed successfully.")
            return
    print("Book not found.")


def search_book():
    keyword = input("Enter search keyword: ")
    matching_books = [book for book in library if keyword.lower() in book["title"].lower()]

    if not matching_books:
        print("No matching books found.")
    else:
        for book in matching_books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Genre:", book["genre"])
            print("ISBN:", book["ISBN"])
            print("Availability:", "Available" if book["availability"] else "Not Available")
            print()







while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Reserve a Book")
    print("7. Process Reservations")
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        reserve_book()
    elif choice == "7":
        process_reservations()
    elif choice == "8":
        print("Thank you for using the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
