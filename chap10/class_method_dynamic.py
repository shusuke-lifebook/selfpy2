from types import MethodType


# 動的に追加するメソッドを準備
def show_first(self) -> None:
    print(f"名前は{self.firstname}です！")


def show_last(self) -> None:
    print(f"苗字は{self.lastname}です！")


# 初期状態では__init__／showメソッドだけ
class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show(self) -> None:
        print(f"私の名前は{self.lastname}{self.firstname}です！")


if __name__ == "__main__":
    p1 = Person("太郎", "山田")
    p2 = Person("次郎", "鈴木")
    Person.show_first = show_first  # type: ignore
    p1.show_last = MethodType(show_last, p1)  # type: ignore
    p1.show_first()  # type: ignore
    p1.show_last()  # type: ignore
    p2.show_first()  # type: ignore
    p2.show_last()  # type: ignore # エラー
