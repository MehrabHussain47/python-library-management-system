from library import Library

library = Library()

while True:

    print("\n=========================================")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=========================================")

    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Show All Members")
    print("7. Search Book")
    print("8. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("\n----- Add New Book -----")

            title = input("Enter Book Title : ")
            author = input("Enter Author : ")
            isbn = input("Enter ISBN : ")

            library.add_book(title, author, isbn)

        elif choice == 2:

            print("\n----- Register Member -----")

            member_id = input("Enter Member ID : ")
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))

            library.register_member(member_id, name, age)

        elif choice == 3:

            print("\n------ Borrow Book ------")

            member_id = input("Enter Member ID : ")
            isbn = input("Enter Book ISBN : ")

            library.borrow_book(member_id, isbn)

        elif choice == 4:

            print("\n------ Return Book ------")

            member_id = input("Enter Member ID : ")
            isbn = input("Enter Book ISBN : ")

            library.return_book(member_id, isbn)

        elif choice == 5:

            library.show_books()

        elif choice == 6:

            library.show_members()

        elif choice == 7:

            print("\n------ Search Book ------")

            title = input("Enter Book Title : ")

            library.search_book(title)

        elif choice == 8:

            print("Thank you for using Library Management System.")
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice.")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    input("\nPress Enter to continue...")