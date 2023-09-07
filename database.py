import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        # Establish a connection to the database
        self.connection = sqlite3.connect(self.db_name)
        # Create necessary tables if they don't exist
        create_books_table = """
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            isbn TEXT UNIQUE
        )
        """
        create_reviews_table = """
        CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            rating INTEGER,
            comment TEXT,
            FOREIGN KEY (book_id) REFERENCES books (book_id)
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(create_books_table)
        cursor.execute(create_reviews_table)
        self.connection.commit()

    def disconnect(self):
        # Close the database connection
        self.connection.close()

    def execute_query(self, query, params=None):
        # Execute the provided SQL query on the database
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()

    def add_book(self, title, author, isbn):
        # Add a new book to the database
        query = (
            "INSERT INTO books (title, author, isbn) "
            "VALUES (?, ?, ?)"
        )
        params = (title, author, isbn)
        self.execute_query(query, params)

    def delete_book(self, book_id):
        # Delete a book from the database based on its ID
        query = f"DELETE FROM books WHERE book_id = {book_id}"
        self.execute_query(query)

    def add_review(self, book_id, rating, comment):
        # Add a review for a book
        query = (
            "INSERT INTO reviews (book_id, rating, comment) "
            "VALUES (?, ?, ?)"
        )
        params = (book_id, rating, comment)
        self.execute_query(query, params)

    def get_book_reviews(self, book_id):
        # Get all reviews for a specific book
        query = f"SELECT * FROM reviews WHERE book_id = {book_id}"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

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
        print("6. Add a Review")
        print("7. Exit")

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
                print(f"{book_record[0]}. {book_record[1]}")
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
            print("Book Details:")
            print(f"Title: {book_record[1]}")
            print(f"Author: {book_record[2]}")
            print(f"ISBN: {book_record[3]}")
        else:
            print("Book not found.")

    def add_book(self):
        print("")
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")

        self.database.connect()
        self.database.add_book(title, author, isbn)
        self.database.disconnect()

        print("Book added successfully.")

    def delete_book(self):
        print("")
        book_id = int(input("Enter the book ID to delete: "))

        self.database.connect()
        self.database.delete_book(book_id)
        self.database.disconnect()

        print("Book deleted successfully.")

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
                print(f"Book ID: {book_record[0]}")
                print(f"Title: {book_record[1]}")
                print(f"Author: {book_record[2]}")
                print(f"ISBN: {book_record[3]}")
                print("--------------------")
        else:
            print("No books available.")

    def add_review(self):
        print("")
        book_id = int(input("Enter the book ID for the review: "))
        rating = int(input("Enter your rating for the book (1-5): "))
        comment = input("Enter your review comment: ")

        self.database.connect()
        self.database.add_review(book_id, rating, comment)
        self.database.disconnect()

        print("Review added successfully.")

    def exit_program(self):
        print("Thank you for using BooksLibrary")
        print("")

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
                self.add_review()
            elif choice == "7":
                self.exit_program()
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    cli = CLI()
    cli.run()
