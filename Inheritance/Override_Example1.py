"""
This is the example of inheritance with composition example
"""

class Book:
    """
    This class describes about the book
    """
    def __init__(self, author, title):
        """
        Initializes the values
        :param author: arg1 and string
        :param title: arg2 and string
        """
        self.author = author
        self.title = title

    def __str__(self):
        return f"{self.author} and {self.title}"

class EBook(Book):
    """
    This class extends the Book
    """
    def __init__(self, author, title, size):
        """
        Initializes the values
        :param author: arg1 and string
        :param title: arg2 and string
        :param size: arg3 and integer
        """
        super().__init__(author, title)
        self.size = size

    def getSize(self):
        """
        Returns the size of the Book
        :return: returns the integer
        """
        return self.size

class PaperBook(Book):
    """
    This class extends the Book
    """
    def __init__(self, author, title, numofpages):
        """
        Initializes the values
        :param author: arg1 and string
        :param title: arg2 and string
        :param numofpages: arg3 and int
        """
        super().__init__(author, title)
        self.numpages = numofpages

    def getNumPages(self):
        """
        Returns the number of pages
        :return: returns the number
        """
        return self.numpages

#The below is the example of composition

class Library:
    """
    This is the example of the compostion class
    """
    def __init__(self):
        self.books =[]

    def add_book(self, book):
        self.books.append(book)

    def getNumberOfBooks(self):
        return len(self.books)

Book1 =Book('Oddysey', 'Homer')
mypaperbook =PaperBook('Malgudidays', 'Narayan', 500)
myebook = EBook('Python3', 'Gosely', 3)

add_library = Library()
add_library.add_book(Book1)
add_library.add_book(mypaperbook)
add_library.add_book(myebook)

print(add_library.getNumberOfBooks())