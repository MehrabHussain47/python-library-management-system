# Library Management System using Python OOP

## Project Overview

This is a console-based **Library Management System** developed using **Python Object-Oriented Programming (OOP)** concepts. The system allows a librarian to manage books and members, borrow and return books, search for books, and display library information.

This project was created as part of a Python OOP assignment.

---

## Features

- Add new books
- Register new members
- Borrow books
- Return books
- View all books
- View all members
- Search books by title
- Input validation
- Exception handling
- Menu-driven console application

---

## OOP Concepts Used

- Classes and Objects
- Constructors (`__init__`)
- Inheritance
- Method Overriding
- Encapsulation (Private Attributes)
- Properties (`@property`)
- Class Variables
- Class Methods
- Static Methods
- Composition
- Exception Handling

---

## Project Structure

```
LibraryManagementSystem/
│
├── person.py
├── member.py
├── book.py
├── library.py
├── main.py
└── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/python-library-management-system.git
```

2. Open the project folder:

```bash
cd python-library-management-system
```

3. Run the program:

```bash
python main.py
```

---

## Sample Menu

```
LIBRARY MANAGEMENT SYSTEM

1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. Show All Books
6. Show All Members
7. Search Book
8. Exit
```

---

## Validation Rules

- ISBN must be unique.
- Member ID must be unique.
- Age must be greater than 0.
- Book title cannot be empty.
- Author name cannot be empty.
- Prevent borrowing an unavailable book.
- Prevent borrowing the same book twice.

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Git
- GitHub

---

## Author

**Name:** Md. Mehrab Hussain Sumon

**Course:** Python OOP Assignment
