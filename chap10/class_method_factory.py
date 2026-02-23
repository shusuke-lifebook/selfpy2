from typing import Self

import requests


# 書籍情報を取得
class Book:
    def __init__(self, isbn: str, title: str, price: int) -> None:
        self.isbn = isbn
        self.title = title
        self.price = price

    # ISBNコード(isbn)をキーに書籍情報を取得する
    @classmethod
    def get_by_isbn(cls, isbn: str) -> Self:
        # <ISBN コード> .jsonを取得
        res = requests.get(f"https://wings.msn.to/tmp/{isbn}.json")
        bs = res.json()
        # 取得した書籍情報をもとにインスタンスを生成
        return cls(bs["isbn"], bs["title"], bs["price"])


if __name__ == "__main__":
    b = Book.get_by_isbn("978-4-7981-8055-7")
    print(b.title)
