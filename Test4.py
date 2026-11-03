class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrowed(self):
        self.is_borrowed=True
        print(f"{self.title} is borrowed")
    def return_book(self):
            self.is_borrowed=False
            print(f"{self.title} is not borrowed")
book_1=Book("Harry Potter","Rowling")
book_2=Book("Malgudi Days","Narayan")
book_3=Book("Heroes of Olympus","Jacen Reynolds")
book_1.borrowed()
book_1.return_book()
book_2.borrowed()
book_2.return_book()
book_3.borrowed()
book_3.return_book()
    