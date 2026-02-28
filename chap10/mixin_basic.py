class LogMixin:
    # 現在のインスタンス内容を列挙
    def show_attr(self) -> None:
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


# ミックスインを組み込み
class Person(LogMixin):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


if __name__ == "__main__":
    p = Person("鈴木修", 50)
    p.show_attr()
