import math


class Coordinate:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # c(x, y)形式で呼び出せ、距離を求める
    def __call__(self, o_x: float, o_y: float) -> float:
        return math.sqrt((o_x - self.x) ** 2 + (o_y - self.y) ** 2)


if __name__ == "__main__":
    c = Coordinate(10, 20)
    print(c(5, 15))
