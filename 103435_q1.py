# Book Model
# Create a Book class with attributes for `title`, `author`, and `is_borrowed`
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False # Default Value

# LibraryMemnber Model
# Create a LibraryMember class with attributes `name`, `member_id`, and a list for `borrowed_books`
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


# Implement methods in Book to Mark as borrowed
# Using Book class method
def mark_as_borrowed(self):
    if not self.is_borrowed: # Checks if the is_borrowed attribute is False
        self.is_borrowed = True # If not borrowed sets is_borrowed to True
        print(f"The book with the title '{self.title}' by '{self.author}' has been marked as borrowed.")
    else:
        print(f"The book with the title '{self.title}'  by '{self.author}' is already borrowed, Sorry")


# Implement methods in Book to Mark as returned
# Using Book class method
def mark_as_returned(self):
    if self.is_borrowed: # Checks if is_borrowed is True
        self.is_borrowed = False # If book is borrowed sets is_borrowed to False
        print(f"The book with the title '{self.title}' by '{self.author}' has been marked as returned.")
    else:
        print(f"The book with the title '{self.title}' by '{self.author}' was not borrowed.")


# Implement methods in `LibraryMember` to borrow a book (checks if the book is available)
# Purpose: This method allows a LibraryMember instance to borrow a Book if it is not already borrowed.
# Using LibraryMember class method
def borrow_book(self, book):
    if not book.is_borrowed:  # Checks if is_borrowed is True
        book.mark_as_borrowed()  # Marks the book as borrowed
        self.borrowed_books.append(book)  # Adds the book to the member's borrowed list
        print(f"{self.name} has checked out '{book.title}' successfully.")
    else:
        print(f"Unfortunately, '{book.title}' is currently unavailable.")

# Implement methods in `LibraryMember` to return a book
# Using LibraryMember class method
def return_book(self, book):
    if book in self.borrowed_books:  # Checks if the book is in the borrowed list
        book.mark_as_returned()  # Marks the book as returned
        self.borrowed_books.remove(book)  # Removes the book from the member's list
        print(f"{self.name} has returned '{book.title}' . Thank you!")
    else:
        print(f"{self.name} has not borrowed '{book.title}', so it cannot be returned.")


# Implement methods in `LibraryMember` to list borrowed books
def list_borrowed_books(self):
    if self.borrowed_books: # Checks if there are any borrowed books
        print(f"{self.name} has borrowed the following books:")
        for book in self.borrowed_books:
            print(f"- {book.title} by {book.author}")
    else:
        print(f"{self.name} has not checked out any books yet.")


# Write interactive code to allow a member to borrow and return books
def main():

    book1 = Book("5 AM CLUB", "Robert Sharma")
    book2 = Book("Meditiation", "Marcus Aurelius")
    book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
    member = LibraryMember("Ian", "A001")

    while True:
        print("\nLibrary Management System")
        print("1. Borrow a Book")
        print("2. Return a Book")
        # print("3. List Borrowed Books")
        # print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable books:")
            available_books = [
                book for book in [book1, book2, book3] if not book.is_borrowed
            ]
            for idx, book in enumerate(available_books, start=1):
                print(f"{idx}. {book.title} by {book.author}")

            if available_books:
                book_choice = int(input("Enter the book number to borrow: ")) - 1
                if 0 <= book_choice < len(available_books):
                    member.borrow_book(available_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("No books are currently available.")

        elif choice == "2":
            print("\nBorrowed books:")
            if member.borrowed_books:
                for idx, book in enumerate(member.borrowed_books, start=1):
                    print(f"{idx}. {book.title} by {book.author}")

                book_choice = int(input("Enter the book number to return: ")) - 1
                if 0 <= book_choice < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("You have no borrowed books to return.")
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
