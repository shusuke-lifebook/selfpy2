from typing import Any, Self


class MyStack(list):
    def push(self, elem: Any) -> Self:
        self.append(elem)
        return self

    def insert(self) -> None:
        raise RuntimeError("Not Support")


if __name__ == "__main__":
    s = MyStack([10, 20, 30])
    s.push(40)
    print(s.pop())
    print(s)
    # mylist = MyStack([10, 20, 30])
    # mylist.insert(1, 50)
