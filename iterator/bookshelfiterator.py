class BookShelfIterator(object):
    def __init__(self,bookshelf):
        self.__bookshelf = bookshelf
        self.__index = 0

    def has_next(self):
        return self.__index < self.__bookshelf.get_length()

    def get_next(self):
        book = self.__bookshelf.get_book_at(self.__index)
        self.__index += 1
        return book
