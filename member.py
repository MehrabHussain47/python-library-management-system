from person import Person

class Member(Person):

    total_members = 0

    def __init__(self, member_id, name, age):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = []

        Member.total_members += 1

    def borrow_book(self, book):
        if book in self.borrowed_books:
            print("Member already borrowed this book.")
            return False

        self.borrowed_books.append(book)
        return True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False

    def display_info(self):
        print(f"Member ID : {self.member_id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Borrowed Books : {len(self.borrowed_books)}")
        print("-" * 35)

    @classmethod
    def show_total_members(cls):
        print("Total Members :", cls.total_members)

    @staticmethod
    def library_rules():
        print("Maximum books allowed: Unlimited")