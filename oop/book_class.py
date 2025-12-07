# book_class.py

class Book:
    """
    A class representing a book with title, author, and publication year.
    Implements magic methods for initialization, deletion, and string representation.
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance with title, author, and publication year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the book.
        
        Returns:
            str: Formatted string in the format "title by author, published in year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Return an official string representation that could recreate the object.
        
        Returns:
            str: String that represents a valid constructor call
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor method called when the Book instance is about to be destroyed.
        Prints a message indicating the book is being deleted.
        """
        print(f"Deleting {self.title}")