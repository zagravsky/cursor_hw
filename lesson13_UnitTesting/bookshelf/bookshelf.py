class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return 'Book %s by %s' % (self.name, self.author)


class Bookshelf:
    collection = []

    def __init__(self):
        self.description = 'Books count: '
        self.collection.clear()

    def __str__(self):
        return self.description + '%i' % len(self.collection)

    def place_book(self, name, author):
        self.collection.append(Book(name, author))

    def return_count(self):
        return len(self.collection)

    def count_books(self):
        return self.return_count()