
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///books_library.db')

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key = True)
    name = Column(String)

    reviews = relationship('Review', back_populates = 'user')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String)
    serial_number = Column(String, unique=True, nullable=False)

    reviews = relationship('Review', back_populates='book')
    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Float, nullable=False)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='reviews')


# Create the database tables based on the defined models
Base.metadata.create_all(engine)    