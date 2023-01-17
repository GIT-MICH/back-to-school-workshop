import re


class Book:
    @staticmethod
    def check_isbn(isbn):
        isbn = isbn.replace("-", "").replace(" ", "").upper()
        match = re.search(r'^(\d{9})(\d|X)$', isbn)
        if not match:
            return False

        digits = match.group(1)
        check_digit = 10 if match.group(2) == 'X' else int(match.group(2))

        result = sum((i + 1) * int(digit) for i, digit in enumerate(digits))
        return (result % 11) == check_digit

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        check_isbn_10 = Book.check_isbn(self.isbn)
        if check_isbn_10:
            print("""
            ISBN: {},
            is correct?: {}, 
             """.format(self.isbn, check_isbn_10))
        else:
            raise ValueError(f'Wrong ISBN number, {self.isbn}')

    def __str__(self):
        return f"{self.title}, {self.author}, {self.isbn}"
