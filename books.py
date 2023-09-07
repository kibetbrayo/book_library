class Book:
    def __init__(self, book_id, title, author, book_code):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_code = book_code

    def get_book_details(self):
        """Retrieve and display book details."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"book_code: {self.book_id}")

    def update_book_info(self, new_title, new_author, new_book_code):
        """Update the book's title, author, and book_code."""
        self.title = new_title
        self.author = new_author
        self.book_code = new_book_code
        print("Book information updated.")
