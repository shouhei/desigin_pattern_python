class BookShelfIterator(object):
    def __init__(self,bookshelf):
        self.bookshelf = bookshelf
        self.index = 0

    def has_next(self):
        return self.index < self.bookshelf.get_length()

    def get_next(self):
        book = self.bookshelf.get_book_at(self.index)
        self.index += 1
        return book
