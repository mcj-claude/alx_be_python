class Book:
    def __init__(self, title, author, year):
        """
        Constructor for Book class.
        Initializes a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor for Book class.
        Prints "Deleting (title of the book)" upon object deletion.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation of Book class.
        Returns a string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation of Book class.
        Returns a string that would recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"