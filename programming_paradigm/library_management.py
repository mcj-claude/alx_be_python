"""
Library Management System
Implements Book and Library classes to demonstrate OOP concepts in Python.
"""


class Book:
    """A class representing a book in a library."""
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize a Library instance with an empty book collection."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): The book to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title if it's available.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """
        Return a book by title (make it available again).
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """Print all books that are currently available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available.")
            return
        
        for book in available_books:
            print(book)