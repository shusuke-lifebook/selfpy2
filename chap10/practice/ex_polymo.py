from abc import ABC, abstractmethod
from typing import override


class Figure(ABC):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @abstractmethod
    def get_area(self) -> float:
        pass


class Triangle(Figure):
    @override
    def get_area(self) -> float:
        return self.width * self.height / 2


class Square(Figure):
    @override
    def get_area(self) -> float:
        return self.width * self.height


if __name__ == "__main__":
    figs = [
        Triangle(10, 15),
        Square(10, 15),
        Triangle(5, 1),
    ]
    for fig in figs:
        if isinstance(fig, Figure):
            print(f"{fig.__class__} : {fig.get_area()}")
