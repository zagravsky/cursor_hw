import unittest
import mock

from bookshelf.bookshelf import Bookshelf
from bookshelf.bookshelf import Book

bookName = "Steel Rat"
authorName = "Harry Harrison"


class TestBookshelf(unittest.TestCase):
    def test_init_bs(self):
        bs = Bookshelf()
        self.assertIsInstance(bs, Bookshelf)

    def test_init_b(self):
        b = Book(bookName, authorName)
        self.assertIsInstance(b, Book)

    def test_bs_add(self):
        bs = Bookshelf()
        bs.place_book(bookName, authorName)
        self.assertEqual(bs.count_books(), 1)

    def test_bs_print(self):
        bs = Bookshelf()
        bs.place_book(bookName, authorName)
        self.assertEqual(str(bs), 'Books count: 1')

    @mock.patch('bookshelf.bookshelf.Bookshelf.return_count')
    def test_bs_add(self, mock_len):
        bs = Bookshelf()
        bs.place_book(bookName, authorName)
        mock_len.return_value = 5

        self.assertEqual(bs.count_books(), 5)


if __name__ == '__main__':
    unittest.main()
