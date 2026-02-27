class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def show(self) -> None:
        print(f"私の名前は{self.__name}、{self.__age}歳です！")


if __name__ == "__main__":
    p = Person("山田太郎", 15)
    print(p.__age)  # 結果：エラー
    # print(p._Person__age)
