from abc import ABC, abstractmethod
from typing import Protocol, override


class Figure(ABC):
    def __init__(self, widht: float, height: float) -> None:
        self.widht = widht
        self.height = height

    @abstractmethod
    def get_area(self) -> float:
        pass


class Triangle(Figure):
    @override
    def get_area(self) -> float:
        return self.widht * self.height / 2


class Rectangle(Figure):
    @override
    def get_area(self) -> float:
        return self.widht * self.height


class Areable(Protocol):
    def get_area(self) -> float: ...


class Japan:
    def get_area(self) -> float:
        return 378000


def show_area(figure: Areable) -> None:
    print(f"{figure.__class__.__name__}の面積は{figure.get_area()}です。")


if __name__ == "__main__":
    show_area(Triangle(10, 15))
    show_area(Rectangle(10, 15))
    show_area(Japan())
