from book import Book
from bookshelf import BookShelf

book_shelf = BookShelf()
titles=['Around the World in 80 days','Bible','Cinderella','Daddy-Long-Leg']
for title in titles:
    book_shelf.append_book(Book(title))

it = book_shelf.iterator()
while it.has_next():
    book = it.get_next()
    print(book.name)
