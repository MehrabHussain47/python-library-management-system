from book import Book
from member import Member

class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):

        for book in self.books:
            if book.isbn == isbn:
                raise ValueError("ISBN already exists.")

        if title.strip() == "":
            raise ValueError("Book title cannot be empty.")

        if author.strip() == "":
            raise ValueError("Author name cannot be empty.")

        book = Book(title, author, isbn)
        self.books.append(book)

        print("Book added successfully!")

    def register_member(self, member_id, name, age):

        for member in self.members:
            if member.member_id == member_id:
                raise ValueError("Member ID already exists.")

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        member = Member(member_id, name, age)
        self.members.append(member)

        print("Member registered successfully!")

    def borrow_book(self, member_id, isbn):

        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m

        if member is None:
            print("Member not found.")
            return

        for b in self.books:
            if b.isbn == isbn:
                book = b

        if book is None:
            print("Book not found.")
            return

        if not book.available:
            print("Sorry! This book is currently unavailable.")
            return

        if book in member.borrowed_books:
            print("Member already borrowed this book.")
            return

        member.borrow_book(book)
        book.available = False

        print("Book borrowed successfully.")

    def return_book(self, member_id, isbn):

        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m

        if member is None:
            print("Member not found.")
            return

        for b in self.books:
            if b.isbn == isbn:
                book = b

        if book is None:
            print("Book not found.")
            return

        if member.return_book(book):
            book.available = True
            print("Book returned successfully.")
        else:
            print("This member did not borrow this book.")

    def show_books(self):

        if len(self.books) == 0:
            print("No books found.")
            return

        print("------------- BOOK LIST -------------")

        for book in self.books:
            book.display_book()

    def show_members(self):

        if len(self.members) == 0:
            print("No members found.")
            return

        print("----------- MEMBER LIST ------------")

        for member in self.members:
            member.display_info()

    def search_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():
                print("Book Found!")
                book.display_book()
                return

        print("Book not found.")