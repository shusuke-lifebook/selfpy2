class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.__firstname = firstname
        self.__lastname = lastname

    # インスタンスの文字列表現を生成
    def __str__(self) -> str:
        return f"{self.lastname} {self.firstname}"

    def __repr__(self) -> str:
        return f"Person('{self.firstname}', '{self.lastname}')"

    @property
    def firstname(self) -> str:
        return self.__firstname

    @property
    def lastname(self) -> str:
        return self.__lastname


if __name__ == "__main__":
    p = Person("太郎", "山田")
    print(p)
