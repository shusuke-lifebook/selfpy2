class Person:
    __slots__ = ["firstname", "lastname", "age"]

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname


if __name__ == "__main__":
    p = Person("太郎", "山田")
    p.age = 18
    p.height = 178  # type: ignore # エラー
