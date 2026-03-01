class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    # 氏／名ともに等しければ同値とする
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Person):
            return self.firstname == other.firstname and self.lastname == other.lastname
        return False


class BusinessPerson(Person):
    def __init__(self, firstname: str, lastname: str, title: str) -> None:
        super().__init__(firstname, lastname)
        # titleを追加
        self.title = title

    def __eq__(self, other: object) -> bool:
        if isinstance(other, BusinessPerson):
            return super().__eq__(other) and self.title == other.title
        return False


if __name__ == "__main__":
    p = Person("太郎", "山田")
    bp = BusinessPerson("太郎", "山田", "部長")
    print(p == bp)
    print(bp == p)
