class MyClass:
    def __init__(self, kind: str, name: str) -> None:
        self.kind = kind
        self.name = name

    def show(self) -> str:
        return f"ペットの{self.kind}の名前は、{self.name}です。"


class MySubClass(MyClass):
    def show(self) -> str:
        return f"[{super().show()}]"


if __name__ == "__main__":
    ms = MySubClass("ハムスター", "のどか")
    print(ms.show())
