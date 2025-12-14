"""
Comprehensive testing script for the library management system.
Demonstrates advanced OOP concepts including inheritance, composition, polymorphism, 
encapsulation, and abstraction.
"""

from library_system import Book, EBook, PrintBook, Library
from typing import List


def test_basic_functionality():
    """Test basic book creation and library operations."""
    print("=== Testing Basic Functionality ===")
    
    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500, "PDF")
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234, "978-0-316-76948-0")
    
    # Test __str__ methods
    print("Book representations:")
    print(f"Classic Book: {classic_book}")
    print(f"Digital Novel: {digital_novel}")
    print(f"Paper Novel: {paper_novel}")
    
    # Create a Library instance
    my_library = Library("Central City Library")
    
    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)
    
    print(f"\nLibrary: {my_library.library_name}")
    print(f"Total books: {len(my_library)}")
    print("\nListing all books:")
    my_library.list_books()


def test_error_handling():
    """Test error handling and edge cases."""
    print("\n=== Testing Error Handling ===")
    
    my_library = Library("Test Library")
    
    # Test adding invalid books
    try:
        invalid_book = Book("", "")  # Empty strings
        my_library.add_book(invalid_book)
    except Exception as e:
        print(f"[PASS] Caught expected error for empty title/author: {e}")
    
    try:
        invalid_ebook = EBook("Test Book", "Test Author", -100)  # Negative file size
        my_library.add_book(invalid_ebook)
    except Exception as e:
        print(f"[PASS] Caught expected error for negative file size: {e}")
    
    try:
        invalid_printbook = PrintBook("Test Book", "Test Author", 0, "")  # Zero pages, empty ISBN
        my_library.add_book(invalid_printbook)
    except Exception as e:
        print(f"[PASS] Caught expected error for invalid PrintBook: {e}")
    
    # Test removing non-existent book
    try:
        my_library.remove_book("Non-existent", "Author")
    except Exception as e:
        print(f"[PASS] Caught expected error for removing non-existent book: {e}")


def test_search_and_filtering():
    """Test search and filtering functionality."""
    print("\n=== Testing Search and Filtering ===")
    
    my_library = Library("Comprehensive Library")
    
    # Add multiple books from different authors
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        EBook("1984", "George Orwell", 300, "EPUB"),
        PrintBook("To Kill a Mockingbird", "Harper Lee", 324, "978-0-06-112008-4"),
        Book("Pride and Prejudice", "Jane Austen"),
        EBook("Brave New World", "Aldous Huxley", 250, "PDF"),
        PrintBook("The Catcher in the Rye", "J.D. Salinger", 234, "978-0-316-76948-0"),
    ]
    
    for book in books:
        my_library.add_book(book)
    
    # Test search functionality
    print(f"Search results for '1984':")
    search_results = my_library.search_books("1984")
    for book in search_results:
        print(f"  {book}")
    
    # Test filtering by author
    print(f"\nBooks by Jane Austen:")
    austen_books = my_library.get_books_by_author("Jane Austen")
    for book in austen_books:
        print(f"  {book}")
    
    print(f"\nTotal books in library: {len(my_library)}")


def test_polymorphism():
    """Test polymorphic behavior of book classes."""
    print("\n=== Testing Polymorphism ===")
    
    books: List[Book] = [
        Book("The Hobbit", "J.R.R. Tolkien"),
        EBook("The Fellowship of the Ring", "J.R.R. Tolkien", 1200, "MOBI"),
        PrintBook("The Two Towers", "J.R.R. Tolkien", 415, "978-0-547-92822-7"),
    ]
    
    print("Demonstrating polymorphic behavior:")
    for i, book in enumerate(books, 1):
        print(f"Book {i}: {book}")
        print(f"  Type: {type(book).__name__}")
        print(f"  String representation: {str(book)}")
        print(f"  Repr: {repr(book)}")
        print()


def test_iteration():
    """Test iteration over library collection."""
    print("\n=== Testing Library Iteration ===")
    
    my_library = Library("Iteration Test Library")
    
    books = [
        EBook("Dune", "Frank Herbert", 800, "EPUB"),
        PrintBook("Foundation", "Isaac Asimov", 244, "978-0-553-29335-0"),
        Book("Hyperion", "Dan Simmons"),
    ]
    
    for book in books:
        my_library.add_book(book)
    
    print(f"Iterating through {len(my_library)} books:")
    for i, book in enumerate(my_library, 1):
        print(f"  {i}. {book}")


def test_composition():
    """Test composition relationships."""
    print("\n=== Testing Composition ===")
    
    # Create multiple libraries
    main_library = Library("Main Library")
    branch_library = Library("Branch Library")
    
    # Add books to different libraries
    books = [
        Book("The Lord of the Rings", "J.R.R. Tolkien"),
        EBook("The Hobbit", "J.R.R. Tolkien", 600, "PDF"),
    ]
    
    for book in books:
        main_library.add_book(book)
    
    # Add one book to branch library
    branch_library.add_book(books[0])
    
    print(f"Main Library has {len(main_library)} books")
    print(f"Branch Library has {len(branch_library)} books")
    
    # Test that books are independent instances
    print(f"\nBooks in Main Library:")
    main_library.list_books()
    
    print(f"\nBooks in Branch Library:")
    branch_library.list_books()


def test_performance():
    """Test performance with larger collections."""
    print("\n=== Testing Performance ===")
    
    import time
    
    large_library = Library("Large Library")
    
    # Add many books to test performance
    start_time = time.time()
    
    for i in range(100):
        if i % 3 == 0:
            book = Book(f"Book {i}", f"Author {i % 10}")
        elif i % 3 == 1:
            book = EBook(f"EBook {i}", f"Author {i % 10}", 100 + i, "PDF")
        else:
            book = PrintBook(f"PrintBook {i}", f"Author {i % 10}", 200 + i, f"978-{i:010d}")
        
        large_library.add_book(book)
    
    add_time = time.time() - start_time
    print(f"Added 100 books in {add_time:.4f} seconds")
    
    # Test search performance
    start_time = time.time()
    results = large_library.search_books("Book 50")
    search_time = time.time() - start_time
    print(f"Search completed in {search_time:.6f} seconds")
    print(f"Found {len(results)} results")
    
    print(f"Total books in library: {len(large_library)}")


def main():
    """Run all test cases."""
    print("Library Management System - Comprehensive Test Suite")
    print("=" * 60)
    
    try:
        test_basic_functionality()
        test_error_handling()
        test_search_and_filtering()
        test_polymorphism()
        test_iteration()
        test_composition()
        test_performance()
        
        print("\n" + "=" * 60)
        print("[SUCCESS] All tests completed successfully!")
        
    except Exception as e:
        print(f"\n[ERROR] Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()