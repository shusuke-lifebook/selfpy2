from __future__ import annotations


class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Coordinate同士の加算
    def __add__(self, other: Coordinate) -> Coordinate:
        return Coordinate(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    # Coordinate同士の加算
    c1 = Coordinate(10.5, 20.5)
    c2 = Coordinate(15.5, 25.5)
    print(c1 + c2)
