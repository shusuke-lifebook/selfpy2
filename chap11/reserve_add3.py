from __future__ import annotations


class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Coordinate同士の加算
    def __add__(self, other: Coordinate | float) -> Coordinate:
        if isinstance(other, Coordinate):
            return Coordinate(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Coordinate(self.x + other, self.y)
        else:
            raise TypeError("type must be Coordiate or float")

    def __iadd__(self, other: Coordinate) -> Coordinate:
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    # Coordinate同士の加算
    c1 = Coordinate(10.5, 20.5)
    c2 = Coordinate(15.5, 25.5)
    c1 += c2
    print(c1)
