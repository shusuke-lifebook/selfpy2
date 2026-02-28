from abc import ABC, abstractmethod
from typing import override


class Figure(ABC):
    # width、heightを準備
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    # 面積を取得(ダミー)
    @abstractmethod
    def get_area(self) -> float:
        pass


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
    # Figure発生クラスのリストを準備
    figs = [Triangle(10, 15), Rectangle(10, 15), Triangle(5, 1)]
    # 配列figsの内容を順番に処理
    for fig in figs:
        if isinstance(fig, Figure):
            print(f"{fig.__class__} : {fig.get_area()}")
