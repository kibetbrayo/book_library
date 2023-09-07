import click
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String)
    book_code = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', book_code='{self.book_code}')>"

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='reviews')

    def __repr__(self):
        return f"<Review(rating={self.rating}, comment='{self.comment}')>"

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """Books Library Management System CLI."""
    pass


@cli.command()
def list_all_books():
    """List all books in the library."""
    books = session.query(Book).all()
    if not books:
        click.echo('No books in the library.')
    else:
        click.echo('List of Books:')
        for book in books:
            click.echo(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Book Code: {book.book_code}')

@cli.command()
@click.option('--title', prompt='Enter book title', help='Title of the book')
@click.option('--author', prompt='Enter author name', help='Author of the book')
@click.option('--book_code', prompt='Enter book_code', help='book_code of the book')
def add_book(title, author, book_code):
    """Add a book to the library."""
    book = Book(title=title, author=author, book_code=book_code)
    session.add(book)
    session.commit()
    click.echo(f'Book added with ID: {book.id}')

@cli.command()
def list_books():
    """List all books in the library."""
    books = session.query(Book).all()
    if not books:
        click.echo('No books in the library.')
    else:
        for book in books:
            click.echo(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, book_code: {book.book_code}')

@cli.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    """Delete a book from the library by ID."""
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        click.echo(f'Book with ID {book_id} deleted successfully.')
    else:
        click.echo(f'Book with ID {book_id} not found.')

@cli.command()
@click.argument('user_id', type=int)
def delete_user(user_id):
    """Delete a user from the library system by ID."""
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        click.echo(f'User with ID {user_id} deleted successfully.')
    else:
        click.echo(f'User with ID {user_id} not found.')

@cli.command()
@click.argument('review_id', type=int)
def delete_review(review_id):
    """Delete a review from the library by ID."""
    review = session.query(Review).filter_by(id=review_id).first()
    if review:
        session.delete(review)
        session.commit()
        click.echo(f'Review with ID {review_id} deleted successfully.')
    else:
        click.echo(f'Review with ID {review_id} not found.')

if __name__ == '__main__':
    cli()
