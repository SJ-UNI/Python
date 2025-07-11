library_books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    book = {"title": title, "author": author, "year": year}
    library_books.append(book)
    print("Book added successfully!")

def view_books():
    if not library_books:
        print("There are no books in the library.")
    else:
        for book in library_books:
            print(f"Title: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\n")

def search_book():
    title = input("Enter book title: ")
    for book in library_books:
        if book['title'] == title:
            print(f"Title: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\n")
            return
    print(f"Book '{title}' not found in the library.")

def remove_book():
    title = input("Enter book title: ")
    for book in library_books:
        if book['title'] == title:
            library_books.remove(book)
            print(f"Book '{title}' removed from the library.")
            return
    print(f"Book '{title}' not found in the library.")

while True:
    print("\nLibrary Management System\n")
    print("1. Add Book\n2. View Books\n3. Search Book\n4. Remove Book\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
