class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    # インスタンス変数の内容を出力
    def show(self) -> None:
        print(f"私の名前は{self.lastname}{self.firstname}です！")


if __name__ == "__main__":
    p = Person("太郎", "山田")
    p.show()
