class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # プロパティ(取得用)
    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    # プロパティ(値設定)
    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @age.setter
    def age(self, value: int) -> None:
        if value <= 0:
            raise ValueError("ageは正数で指定します。")
        self.__age = value


if __name__ == "__main__":
    p = Person("山田太郎", 15)
    p.name = "鈴木次郎"
    p.age = 35
    print(p.name)
    print(p.age)
