from typing import override


class Top:
    def hoge(self) -> None:
        print("TopA")


class MiddleA(Top):
    @override
    def hoge(self) -> None:
        print("MiddleA")


class MiddleB(Top):
    @override
    def hoge(self) -> None:
        print("MiddleB")


class Low(MiddleA, MiddleB):
    pass


if __name__ == "__main__":
    lo = Low()
    lo.hoge()  # MiddleA
