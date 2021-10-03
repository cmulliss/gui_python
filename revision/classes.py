class Book:
    TYPES = ("hardcover", "paperback", "kindle")

    # because Book is a class
    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    # create repr method  to make it easier
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

    @classmethod
    def kindle(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[2], page_weight)


book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
other = Book.kindle("Python for beginners", 0)


print(book)
print(light)
print(other)

# Book is cls so use that instead in classmethods.
# -> "Book": returns a Book object
