import pickle

from booke import Book

b = Book("978-4-7981-5382-7", "独習C#新版", 3600)

with open("./chap07/book.bin", "wb") as file:
    pickle.dump(b, file)
