from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Database  
from books import Book  

Base = declarative_base()
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class CLI:
    def __init__(self):
        self.database = Database("library.db")

    def show_menu(self):
        print("")
        print("Welcome to BooksLibrary!")
        print("1. Browse Books in the library")
        print("2. View Book Details")
        print("3. Add a Book Title")
        print("4. Delete Book in the library")
        print("5. List All Books")
        print("6. Exit")

    def browse_books(self):
        print("")
        self.database.connect()
        query = "SELECT * FROM books"
        cursor = self.database.connection.cursor()
        cursor.execute(query)
        book_records = cursor.fetchall()
        self.database.disconnect()

        if len(book_records) > 0:
            print("Available Books:")
            for book_record in book_records:
                book = Book(*book_record)
                print(f"{book.book_id}. {book.title}")
        else:
            print("No books available.")

    def view_book_details(self):
        print("")
        book_id = int(input("Enter the book ID: "))

        self.database.connect()
        query = f"SELECT * FROM books WHERE book_id = {book_id}"
        cursor = self.database.connection.cursor()
        cursor.execute(query)
        book_record = cursor.fetchone()

        if book_record is not None:
            book = Book(*book_record)
            book.get_book_details()
        else:
            print("Book not found.")

    def add_book(self):
        print("")
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        book_code = input("Enter the book_code of the book: ")

        self.database.connect()
        self.database.add_book(title, author, book_code)
        self.database.disconnect()

        print("Book added successfully.")

    def delete_book(self):
        print("")
        book_id = int(input("Enter the book ID to delete: "))

        self.database.connect()
        self.database.delete_book(book_id)
        self.database.disconnect()

        print("Book deleted successfully.")

    def exit_program(self):
        print("Thank you for using BooksLibrary")
        print("")

    def list_all_books(self):
        print("List of All Books:")
        self.database.connect()
        query = "SELECT * FROM books"
        cursor = self.database.connection.cursor()
        cursor.execute(query)
        book_records = cursor.fetchall()
        self.database.disconnect()

        if len(book_records) > 0:
            for book_record in book_records:
                book = Book(*book_record)
                print(f"Book ID: {book.book_id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Book Code: {book.book_code}")
                print("")
        else:
            print("No books available.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.browse_books()
            elif choice == "2":
                self.view_book_details()
            elif choice == "3":
                self.add_book()
            elif choice == "4":
                self.delete_book()
            elif choice == "5":
                self.list_all_books()
            elif choice == "6":
                self.exit_program()
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    cli = CLI()
    cli.run()
