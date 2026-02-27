class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    # nameのゲッター
    def get_name(self) -> str:
        return self.__name

    # ageのゲッター
    def get_age(self) -> int:
        return self.__age

    # nameのセッター
    def set_name(self, value: str) -> None:
        self.__name = value

    # ageのセッター
    def set_age(self, value: int) -> None:
        if value <= 0:
            raise ValueError("ageは正数で指定します。")
        self.__age = value

    def show(self) -> None:
        print(f"私の名前は{self.get_name()}、{self.get_age()}歳です！")


if __name__ == "__main__":
    p = Person("山田太郎", 15)
    p.set_age(35)
    print(p.get_age())
    p.set_age(-15)  # エラー
