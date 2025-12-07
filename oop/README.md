# Library Management System

A comprehensive Python library management system demonstrating advanced object-oriented programming concepts including inheritance, composition, polymorphism, encapsulation, and abstraction.

## Features

### 🎯 Object-Oriented Design Principles
- **Inheritance**: `EBook` and `PrintBook` inherit from base `Book` class
- **Composition**: `Library` class manages collections of books
- **Polymorphism**: Different book types treated uniformly through base class interface
- **Encapsulation**: Private attributes with property decorators for controlled access
- **Abstraction**: Base class provides common interface for all book types

### 📚 Core Functionality
- **Book Management**: Create and manage different types of books
- **Library Operations**: Add, remove, search, and filter books
- **Type Safety**: Comprehensive type hints throughout the codebase
- **Error Handling**: Robust validation and exception handling
- **Logging**: Detailed logging for debugging and monitoring
- **Performance**: Optimized for large collections

### 🔍 Advanced Features
- Search books by title or author
- Filter books by author
- Duplicate detection
- ISBN validation
- Iterator support for easy traversal
- String representations for debugging
- Custom exceptions for better error handling

## Installation

No external dependencies required. This project uses only Python standard library modules.

```bash
# Clone the repository
git clone <repository-url>
cd alx_be_python/oop

# Run the test suite
python main.py
```

## Usage Examples

### Basic Usage

```python
from library_system import Book, EBook, PrintBook, Library

# Create different types of books
classic_book = Book("Pride and Prejudice", "Jane Austen")
digital_novel = EBook("Snow Crash", "Neal Stephenson", 500, "PDF")
paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234, "978-0-316-76948-0")

# Create a library
my_library = Library("Central City Library")

# Add books to the library
my_library.add_book(classic_book)
my_library.add_book(digital_novel)
my_library.add_book(paper_novel)

# List all books
my_library.list_books()
```

### Advanced Features

```python
from library_system import Library

# Create library
library = Library("Advanced Library")

# Add multiple books
books = [
    Book("1984", "George Orwell"),
    EBook("Brave New World", "Aldous Huxley", 300, "EPUB"),
    PrintBook("Fahrenheit 451", "Ray Bradbury", 158, "978-0-307-29020-5")
]

for book in books:
    library.add_book(book)

# Search functionality
results = library.search_books("1984")
for book in results:
    print(f"Found: {book}")

# Filter by author
orwell_books = library.get_books_by_author("George Orwell")
print(f"Books by George Orwell: {len(orwell_books)}")

# Iterate through collection
for book in library:
    print(f"Iterating: {book}")

# Check library size
print(f"Total books: {len(library)}")
```

### Error Handling

```python
from library_system import Book, Library, BookValidationError

try:
    # This will raise a validation error
    invalid_book = Book("", "Anonymous")
except BookValidationError as e:
    print(f"Validation error: {e}")

try:
    library = Library("Test Library")
    library.add_book(Book("Test", "Author"))
    library.add_book(Book("Test", "Author"))  # Duplicate
except BookValidationError as e:
    print(f"Duplicate error: {e}")
```

### Class Methods and Static Methods

```python
from library_system import Library

# Create empty library using class method
empty_lib = Library.create_empty_library("New Branch")

# Validate ISBN format
is_valid = Library.validate_isbn_format("978-0-316-76948-0")
print(f"ISBN validation: {is_valid}")
```

## API Reference

### Book Class

Base class for all book types.

**Attributes:**
- `title` (str): Book title
- `author` (str): Book author

**Methods:**
- `__str__()`: String representation
- `__repr__()`: Detailed representation
- `__eq__()`: Equality comparison
- `__hash__()`: Hash generation

### EBook Class

Electronic book with file attributes.

**Additional Attributes:**
- `file_size` (int): File size in KB
- `file_format` (str): File format (PDF, EPUB, etc.)

**Methods:**
- `get_file_info()`: Get formatted file information

### PrintBook Class

Physical book with print attributes.

**Additional Attributes:**
- `page_count` (int): Number of pages
- `isbn` (str): International Standard Book Number

**Methods:**
- `get_physical_info()`: Get formatted physical book information

### Library Class

Manages a collection of books.

**Attributes:**
- `library_name` (str): Name of the library
- Books collection (private)

**Methods:**
- `add_book(book)`: Add a book to the library
- `remove_book(title, author)`: Remove a book from the library
- `search_books(query)`: Search for books
- `get_books_by_author(author)`: Get books by author
- `get_total_books()`: Get total book count
- `list_books()`: Display all books
- `__len__()`: Support for len() function
- `__iter__()`: Support for iteration

**Class Methods:**
- `create_empty_library(name)`: Create empty library

**Static Methods:**
- `validate_isbn_format(isbn)`: Validate ISBN format

## File Structure

```
alx_be_python/oop/
├── library_system.py    # Main implementation
├── main.py             # Comprehensive test suite
└── README.md           # This documentation
```

## Testing

Run the comprehensive test suite:

```bash
python main.py
```

The test suite includes:
- Basic functionality tests
- Error handling tests
- Search and filtering tests
- Polymorphism demonstration
- Iterator testing
- Composition testing
- Performance testing

## Design Patterns Used

1. **Template Method**: Base `Book` class defines structure for derived classes
2. **Strategy Pattern**: Different book types with specialized behaviors
3. **Iterator Pattern**: Library class supports iteration over books
4. **Factory Pattern**: Class methods for creating library instances
5. **Data Transfer Object**: Book classes encapsulate book data

## Best Practices Implemented

- ✅ Type hints throughout the codebase
- ✅ Comprehensive docstrings (Google-style)
- ✅ Input validation and error handling
- ✅ Proper exception hierarchy
- ✅ Property decorators for encapsulation
- ✅ String representations (`__str__`, `__repr__`)
- ✅ Equality and hashing methods
- ✅ Iterator support
- ✅ Logging for debugging
- ✅ Performance considerations
- ✅ PEP 8 compliance

## Requirements

- Python 3.7+
- No external dependencies

## License

This project is part of the ALX Backend Python curriculum.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## Performance Considerations

The library is optimized for:
- Fast book addition and removal
- Efficient search operations
- Memory-efficient book storage
- Scalability for large collections (1000+ books)

## Future Enhancements

Potential improvements:
- Database integration for persistence
- Web interface for library management
- Advanced search with filters
- Book borrowing/returning system
- User management
- Report generation
- Export to various formats (JSON, CSV, etc.)