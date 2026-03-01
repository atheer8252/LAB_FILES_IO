import json

FILE_NAME = "books.json"


# ---------- File Handling ----------

def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# ---------- Book Operations ----------

def add_book():
    books = load_books()

    isbn = input("Enter ISBN: ")

    # Check duplicate ISBN
    for book in books:
        if book["isbn"] == isbn:
            print("Book already exists!")
            return

    title = input("Enter title: ")
    author = input("Enter author: ")

    new_book = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "status": "available"
    }

    books.append(new_book)
    save_books(books)

    print("Book added successfully!")


def display_books():
    books = load_books()

    if not books:
        print("No books found.")
        return

    for book in books:
        print("--------------------------------")
        print(f"ISBN   : {book['isbn']}")
        print(f"Title  : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Status : {book['status']}")
    print("--------------------------------")


def search_books():
    books = load_books()

    keyword = input("Enter ISBN or title to search: ").lower()

    found = False

    for book in books:
        if keyword in book["isbn"].lower() or keyword in book["title"].lower():
            print("--------------------------------")
            print(f"ISBN   : {book['isbn']}")
            print(f"Title  : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Status : {book['status']}")
            found = True

    if not found:
        print("Book not found.")


def delete_book():
    books = load_books()

    isbn = input("Enter ISBN to delete: ")

    new_books = [book for book in books if book["isbn"] != isbn]

    if len(new_books) == len(books):
        print("Book not found.")
    else:
        save_books(new_books)
        print("Book deleted successfully!")


def borrow_book():
    books = load_books()

    isbn = input("Enter ISBN to borrow: ")

    for book in books:
        if book["isbn"] == isbn:
            if book["status"] == "available":
                book["status"] = "borrowed"
                save_books(books)
                print("Book borrowed successfully!")
                return
            else:
                print("Book is already borrowed.")
                return

    print("Book not found.")


def return_book():
    books = load_books()

    isbn = input("Enter ISBN to return: ")

    for book in books:
        if book["isbn"] == isbn:
            if book["status"] == "borrowed":
                book["status"] = "available"
                save_books(books)
                print("Book returned successfully!")
                return
            else:
                print("Book was not borrowed.")
                return

    print("Book not found.")


# ---------- Menu ----------

def menu():
    while True:
        print("\n===== Library Menu =====")
        print("1. Add book")
        print("2. Display books")
        print("3. Search books")
        print("4. Delete book")
        print("5. Borrow book")
        print("6. Return book")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            borrow_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()