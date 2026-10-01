from books import book
from users import user
from library import library

# instances
book1 = book("001", "OOP Fundamentals", "Jhon L", "BBC")
book2 = book("002", "Python for dummies", "Stef Maruzh", "For dummies")
user1 = user("001", "Dylan Percy", "1234")
library = library()
library.add_book(book1)
library.add_book(book2)
library.add_users(user1)
library.show_books()
# Requeriments
# 1. The system must allow register books.
# 2. The system must allow register users.
# 4. A book that has already been borrowed cannot be borrowed again
# 5. The system must allow a book to be returned.
# 3. The system must allow a book to be borrowed by a user.
