class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show(self) -> None:
        print(f"私の名前は{self.lastname}{self.firstname}です！")


# Personを継承したBusinessPersonクラスを定義
class BusinessPerson(Person):
    def work(self) -> None:
        print(f"{self.lastname}{self.firstname}は働いています。")


class HetareBusinessPerson(BusinessPerson):
    def work(self) -> None:
        super().work()
        print("ただし、ボチボチです。")


if __name__ == "__main__":
    hbp = HetareBusinessPerson("太郎", "山田")
    hbp.work()
    hbp.show()
