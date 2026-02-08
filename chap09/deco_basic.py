from collections.abc import Callable
from typing import Any


def log_func(func: Callable[..., Any]) -> Callable[..., Any]:
    # 関数内関数を定義
    def inner(*args, **keywds):
        print("----------")
        print(f"Name: {func.__name__}")
        print(f"Args: {args}")
        print(f"Keywds: {keywds}")
        print("----------")
        return func(*args, **keywds)

    return inner


@log_func
def hoge(x: int, y: int, m: str = "bar", n: str = "piyo") -> None:
    print(f"hoge: {x}-{y}/{m}-{n}")


hoge(15, 37, m="ほげ", n="ぴょ")
