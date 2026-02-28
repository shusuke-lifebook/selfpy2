from typing import final, override


class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show(self) -> None:
        print(f"私の名前は{self.lastname}{self.firstname}です！")


# Personを継承したBusinessPersonクラスを定義
class BusinessPerson(Person):
    @final
    def work(self) -> None:
        print(f"{self.lastname}{self.firstname}は働いています。")


@final
class EliteBusinessPerson(BusinessPerson):
    @override
    def work(self) -> None:
        print(f"{self.lastname}{self.firstname}はバリバリ働いています。")


if __name__ == "__main__":
    bp = EliteBusinessPerson("太郎", "山田")
    bp.work()
    bp.show()
