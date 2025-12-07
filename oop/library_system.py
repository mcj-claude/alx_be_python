"""
Advanced Library Management System

This module implements a comprehensive library management system demonstrating
advanced object-oriented programming concepts including inheritance, composition,
polymorphism, encapsulation, and abstraction.

Classes:
    Book: Base class representing a generic book
    EBook: Electronic book with file size and format
    PrintBook: Physical book with page count and ISBN
    Library: Manages a collection of books using composition
"""

from typing import List, Optional, Union
import logging
from dataclasses import dataclass


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class BookValidationError(Exception):
    """Custom exception for book validation errors."""
    message: str


class Book:
    """
    Base class representing a generic book.
    
    This class demonstrates encapsulation and abstraction by providing
    a common interface for all book types.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
    
    Raises:
        BookValidationError: If title or author are invalid
    """
    
    def __init__(self, title: str, author: str) -> None:
        """
        Initialize a Book instance.
        
        Args:
            title: The title of the book
            author: The author of the book
            
        Raises:
            BookValidationError: If title or author are empty or None
        """
        self._validate_title_author(title, author)
        self._title = title.strip()
        self._author = author.strip()
        logger.info(f"Created Book: {self.title} by {self.author}")
    
    def _validate_title_author(self, title: str, author: str) -> None:
        """Validate title and author parameters."""
        if not title or not isinstance(title, str) or not title.strip():
            raise BookValidationError("Title must be a non-empty string")
        if not author or not isinstance(author, str) or not author.strip():
            raise BookValidationError("Author must be a non-empty string")
    
    @property
    def title(self) -> str:
        """Get the book title."""
        return self._title
    
    @property
    def author(self) -> str:
        """Get the book author."""
        return self._author
    
    def __str__(self) -> str:
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the book."""
        return f"Book(title='{self.title}', author='{self.author}')"
    
    def __eq__(self, other) -> bool:
        """Check equality based on title and author."""
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    
    def __hash__(self) -> int:
        """Generate hash based on title and author."""
        return hash((self.title, self.author))


class EBook(Book):
    """
    EBook class inheriting from Book with additional file attributes.
    
    Demonstrates inheritance by extending the Book base class with
    electronic book specific attributes.
    
    Attributes:
        file_size (int): The file size in KB
        file_format (str): The file format (e.g., PDF, EPUB, MOBI)
    """
    
    def __init__(self, title: str, author: str, file_size: int, file_format: str) -> None:
        """
        Initialize an EBook instance.
        
        Args:
            title: The title of the book
            author: The author of the book
            file_size: The file size in KB
            file_format: The file format
            
        Raises:
            BookValidationError: If any parameter is invalid
        """
        super().__init__(title, author)
        self._validate_file_attributes(file_size, file_format)
        self._file_size = file_size
        self._file_format = file_format.strip().upper()
        logger.info(f"Created EBook: {self.title} by {self.author}")
    
    def _validate_file_attributes(self, file_size: int, file_format: str) -> None:
        """Validate file size and format parameters."""
        if not isinstance(file_size, int) or file_size <= 0:
            raise BookValidationError("File size must be a positive integer")
        if not file_format or not isinstance(file_format, str) or not file_format.strip():
            raise BookValidationError("File format must be a non-empty string")
    
    @property
    def file_size(self) -> int:
        """Get the file size in KB."""
        return self._file_size
    
    @property
    def file_format(self) -> str:
        """Get the file format."""
        return self._file_format
    
    def __str__(self) -> str:
        """Return string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB, Format: {self.file_format}"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the EBook."""
        return (f"EBook(title='{self.title}', author='{self.author}', "
                f"file_size={self.file_size}, file_format='{self.file_format}')")
    
    def get_file_info(self) -> str:
        """Get formatted file information."""
        return f"File: {self.file_format}, {self.file_size}KB"


class PrintBook(Book):
    """
    PrintBook class inheriting from Book with additional print attributes.
    
    Demonstrates inheritance by extending the Book base class with
    physical book specific attributes.
    
    Attributes:
        page_count (int): The number of pages
        isbn (str): The International Standard Book Number
    """
    
    def __init__(self, title: str, author: str, page_count: int, isbn: str) -> None:
        """
        Initialize a PrintBook instance.
        
        Args:
            title: The title of the book
            author: The author of the book
            page_count: The number of pages
            isbn: The International Standard Book Number
            
        Raises:
            BookValidationError: If any parameter is invalid
        """
        super().__init__(title, author)
        self._validate_print_attributes(page_count, isbn)
        self._page_count = page_count
        self._isbn = isbn.strip()
        logger.info(f"Created PrintBook: {self.title} by {self.author}")
    
    def _validate_print_attributes(self, page_count: int, isbn: str) -> None:
        """Validate page count and ISBN parameters."""
        if not isinstance(page_count, int) or page_count <= 0:
            raise BookValidationError("Page count must be a positive integer")
        if not isbn or not isinstance(isbn, str) or not isbn.strip():
            raise BookValidationError("ISBN must be a non-empty string")
    
    @property
    def page_count(self) -> int:
        """Get the page count."""
        return self._page_count
    
    @property
    def isbn(self) -> str:
        """Get the ISBN."""
        return self._isbn
    
    def __str__(self) -> str:
        """Return string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}, ISBN: {self.isbn}"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the PrintBook."""
        return (f"PrintBook(title='{self.title}', author='{self.author}', "
                f"page_count={self.page_count}, isbn='{self.isbn}')")
    
    def get_physical_info(self) -> str:
        """Get formatted physical book information."""
        return f"Pages: {self.page_count}, ISBN: {self.isbn}"


class Library:
    """
    Library class demonstrating composition by managing a collection of books.
    
    This class demonstrates composition by containing and managing Book objects.
    It provides advanced functionality for searching, filtering, and managing
    the book collection.
    
    Attributes:
        library_name (str): The name of the library
        _books (List[Book]): Private list to store book instances
    """
    
    def __init__(self, library_name: str = "My Library") -> None:
        """
        Initialize a Library instance.
        
        Args:
            library_name: The name of the library (optional, defaults to "My Library")
            
        Raises:
            BookValidationError: If library_name is invalid
        """
        self._validate_library_name(library_name)
        self._library_name = library_name.strip()
        self.books = []
        self._books: List[Book] = []
        logger.info(f"Created Library: {self.library_name}")
    
    def _validate_library_name(self, library_name: str) -> None:
        """Validate library name parameter."""
        if not library_name or not isinstance(library_name, str) or not library_name.strip():
            raise BookValidationError("Library name must be a non-empty string")
    
    @property
    def library_name(self) -> str:
        """Get the library name."""
        return self._library_name
    
    @library_name.setter
    def library_name(self, name: str) -> None:
        """Set the library name with validation."""
        self._validate_library_name(name)
        self._library_name = name.strip()
    
    @property
    def books(self) -> List[Book]:
        """Get the list of books."""
        return self._books
    
    @books.setter
    def books(self, books_list: List[Book]) -> None:
        """Set the list of books."""
        self._books = books_list
    
    def add_book(self, book: Book) -> None:
        """
        Add a book to the library.
        
        Args:
            book: A Book, EBook, or PrintBook instance
            
        Raises:
            BookValidationError: If book is invalid or already exists
        """
        if not isinstance(book, Book):
            raise BookValidationError("Object must be an instance of Book or its subclasses")
        
        # Check for duplicates
        for existing_book in self._books:
            if existing_book == book:
                raise BookValidationError(f"Book '{book.title}' by {book.author} already exists in the library")
        
        self._books.append(book)
        logger.info(f"Added book to {self.library_name}: {book.title}")
    
    def _validate_title_author(self, title: str, author: str) -> None:
        """Validate title and author parameters."""
        if not title or not isinstance(title, str) or not title.strip():
            raise BookValidationError("Title must be a non-empty string")
        if not author or not isinstance(author, str) or not author.strip():
            raise BookValidationError("Author must be a non-empty string")
    
    def _validate_author(self, author: str) -> None:
        """Validate author parameter only."""
        if not author or not isinstance(author, str) or not author.strip():
            raise BookValidationError("Author must be a non-empty string")
    
    def remove_book(self, title: str, author: str) -> bool:
        """
        Remove a book from the library.
        
        Args:
            title: The title of the book to remove
            author: The author of the book to remove
            
        Returns:
            bool: True if book was removed, False if not found
            
        Raises:
            BookValidationError: If title or author are invalid
        """
        self._validate_title_author(title, author)
        
        for i, book in enumerate(self._books):
            if book.title == title.strip() and book.author == author.strip():
                removed_book = self._books.pop(i)
                logger.info(f"Removed book from {self.library_name}: {removed_book.title}")
                return True
        
        raise BookValidationError(f"Book '{title}' by {author} not found in the library")
    
    def search_books(self, query: str) -> List[Book]:
        """
        Search for books by title or author.
        
        Args:
            query: Search query string
            
        Returns:
            List[Book]: List of matching books
            
        Raises:
            BookValidationError: If query is invalid
        """
        if not query or not isinstance(query, str) or not query.strip():
            raise BookValidationError("Search query must be a non-empty string")
        
        query = query.strip().lower()
        matches = []
        
        for book in self._books:
            if (query in book.title.lower() or 
                query in book.author.lower()):
                matches.append(book)
        
        logger.info(f"Search in {self.library_name} for '{query}' returned {len(matches)} results")
        return matches
    
    def get_books_by_author(self, author: str) -> List[Book]:
        """
        Get all books by a specific author.
        
        Args:
            author: The author's name
            
        Returns:
            List[Book]: List of books by the author
            
        Raises:
            BookValidationError: If author is invalid
        """
        self._validate_author(author)  # Only validate author
        
        author = author.strip()
        author_books = [book for book in self._books if book.author == author]
        
        logger.info(f"Found {len(author_books)} books by {author} in {self.library_name}")
        return author_books
    
    def get_total_books(self) -> int:
        """
        Get the total number of books in the library.
        
        Returns:
            int: Total number of books
        """
        return len(self._books)
    
    def list_books(self) -> None:
        """Print details of each book in the library."""
        if not self._books:
            print(f"No books in {self.library_name}")
            return
        
        print(f"\nBooks in {self.library_name}:")
        print("-" * 50)
        for i, book in enumerate(self._books, 1):
            print(f"{i:2d}. {book}")
    
    def __len__(self) -> int:
        """Return the number of books in the library."""
        return len(self._books)
    
    def __iter__(self):
        """Return iterator over the books."""
        return iter(self._books)
    
    def __str__(self) -> str:
        """Return string representation of the library."""
        return f"Library: {self.library_name} ({len(self)} books)"
    
    def __repr__(self) -> str:
        """Return detailed string representation of the library."""
        return f"Library(library_name='{self.library_name}', total_books={len(self._books)})"
    
    @classmethod
    def create_empty_library(cls, name: str) -> 'Library':
        """
        Create an empty library with a given name.
        
        Args:
            name: The name of the library
            
        Returns:
            Library: New Library instance
        """
        return cls(name)
    
    @staticmethod
    def validate_isbn_format(isbn: str) -> bool:
        """
        Validate ISBN format (basic validation).
        
        Args:
            isbn: ISBN string to validate
            
        Returns:
            bool: True if format is valid, False otherwise
        """
        if not isinstance(isbn, str):
            return False
        
        # Remove hyphens and spaces
        clean_isbn = isbn.replace('-', '').replace(' ', '')
        
        # Check if it's 10 or 13 digits
        return (len(clean_isbn) == 10 or len(clean_isbn) == 13) and clean_isbn.isdigit()


# Type alias for book types
BookType = Union[Book, EBook, PrintBook]