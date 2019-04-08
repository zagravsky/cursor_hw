class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f'Book {self.name} by {self.author}'


class Bookshelf:
    collection = []

    def __init__(self):
        self.description = 'Books count: '
        self.collection.clear()

    def __str__(self):
        return f'{self.description}{len(self.collection)}'

    def place_book(self, name, author):
        self.collection.append(Book(name, author))

    def return_count(self):
        return len(self.collection)

    def count_books(self):
        return self.return_count()