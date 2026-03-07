import math


class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __int__(self) -> int:
        return int(self.__float__())

    def __float__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)


if __name__ == "__main__":
    c = Coordinate(1, 2)
    print(float(c))
    print(int(c))
