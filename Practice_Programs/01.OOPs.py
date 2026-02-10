#1. Book Details Display
'''Problem: Create a Book class with title, author, and price. Add a method to display
all book details.
Answer:'''

class Book:
   def __init__(self, title, author, price):
       self.title = title
       self.author = author
       self.price = price
   def display_info(self):
        print(f"Title: {self.title}, Author: {self.author},Price: ${self.price}")
# Object creation and method call
book1 = Book("Clean Code", "Robert Martin", 450)
book1.display_info()