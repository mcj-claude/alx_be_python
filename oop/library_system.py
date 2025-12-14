class Book:
    """
    Base class representing a generic book.
    Attributes: title (str) and author (str).
    """
    def __init__(self, title, author):
        """
        Initialize a Book instance with title and author.
        """
        self.title = title
        self.author = author


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size attribute.
    """
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        Calls parent class __init__ and adds file_size.
        """
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book and adds page_count attribute.
    """
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        Calls parent class __init__ and adds page_count.
        """
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """
    Class representing a library that manages a collection of books.
    Demonstrates composition by managing Book, EBook, and PrintBook instances.
    """
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a Book, EBook, or PrintBook instance to the library.
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of each book in the library.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")