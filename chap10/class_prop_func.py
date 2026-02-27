class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_name(self, value: str) -> None:
        self.__name = value

    def set_age(self, value: int) -> None:
        if value <= 0:
            raise ValueError("ageは正数で指定します。")
        self.__age = value

    def show(self) -> None:
        print(f"私の名前は{self.get_name()}、{self.get_age()}歳です！")

    name = property(get_name, set_name)
    age = property(get_age, set_age)


if __name__ == "__main__":
    p = Person("山田太郎", 15)
    p.name = "鈴木次郎"
    p.age = 35
    print(p.name)
    print(p.age)
