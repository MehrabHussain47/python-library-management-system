class Book:

    total_books = 0

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True

        Book.total_books += 1

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        self.__available = value

    def display_book(self):
        status = "Available" if self.available else "Borrowed"

        print(f"ISBN : {self.isbn}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")
        print("-" * 35)

    @classmethod
    def show_total_books(cls):
        print("Total Books :", cls.total_books)

    @staticmethod
    def library_name():
        print("ABC Library")