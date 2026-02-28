from typing import override


class TopA:
    def hoge(self) -> None:
        print("TopA")


class TopB:
    def hoge(self) -> None:
        print("TopB")


class MiddleA(TopA, TopB):
    @override
    def hoge(self) -> None:
        print("MiddleA")


# class MiddleB(TopB, TopA):
class MiddleB(TopA, TopB):
    @override
    def hoge(self) -> None:
        print("MiddleB")


class Low(MiddleA, MiddleB):
    pass


if __name__ == "__main__":
    lo = Low()
    lo.hoge()
