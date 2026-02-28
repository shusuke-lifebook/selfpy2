class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f"私の名前は{self.lastname}{self.firstname}です！")


class Foreiger(Person):
    def __init__(self, firstname: str, middlename: str, lastname: str) -> None:
        super().__init__(firstname, lastname)
        self.middlename = middlename

    def show(self):
        print(f"私の名前は{self.lastname}{self.middlename}{self.firstname}です！")


if __name__ == "__main__":
    fr = Foreiger("太郎", "ヨーダ", "山田")
    fr.show()
