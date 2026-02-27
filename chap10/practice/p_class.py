class Pet:
    def __init__(self, kind: str, name: str) -> None:
        self.kind = kind
        self.name = name

    def show(self) -> None:
        print(f"私のペットは{self.kind}の{self.name}ちゃんです！")


if __name__ == "__main__":
    p = Pet("ハムスター", "のどか")
    p.show()
