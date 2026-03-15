from typing import Self


class MyStack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> Self:
        self._items.append(item)
        return self

    def pop(self) -> T:
        return self._items.pop()


if __name__ == "__main__":
    s = MyStack[int]()
    s.push(10).push(20).push(30)
    print(s.pop())
