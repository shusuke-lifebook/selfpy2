from typing import override


class Figure:
    # width、heightを準備
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    # 面積を取得(ダミー)
    def get_area(self) -> float:
        return 0.0


class Triangle(Figure):
    # 三角形の面積を求めるためのget_areaメソッドを定義
    @override
    def get_area(self) -> float:
        return self.width * self.height / 2


class Rectangle(Figure):
    # 四角形の面積を求めるためのget_areaメソッドを定義
    @override
    def get_area(self) -> float:
        return self.width * self.height


if __name__ == "__main__":
    t = Triangle(10, 15)
    r = Rectangle(10, 15)
    print(t.get_area())
    print(r.get_area())
