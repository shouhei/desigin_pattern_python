from bookshelfiterator import BookShelfIterator
class BookShelf(object):
    def __init__(self):
        self.__books = []
        self.__last = 0

    def get_book_at(self,index):
        return self.__books[index]

    def append_book(self,book):
        self.__books.append(book)
        self.__last += 1

    def get_length(self):
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)
