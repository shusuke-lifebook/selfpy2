from __future__ import annotations


class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # 「<」ルール
    def __lt__(self, other: Coordinate) -> bool:
        return self.x**2 + self.y**2 < other.x**2 + other.y**2

    # 「<=」 ルール
    def __le__(self, other: Coordinate) -> bool:
        return self.x**2 + self.y**2 <= other.x**2 + other.y**2

    # 「>」 ルール
    def __gt__(self, other: Coordinate) -> bool:
        return not self.__le__(other)

    # 「>=」ルール
    def __ge__(self, other: Coordinate) -> bool:
        return not self.__le__(other)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    c1 = Coordinate(1, 2)
    c2 = Coordinate(15, 25)
    c3 = Coordinate(2, 1)
    print(c1 < c2)
    print(c1 <= c3)
    print(c1 <= c2)
    print(c1 > c2)
