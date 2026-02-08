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


def hoge(x: int, y: int, m: str = "bar", n: str = "piyo") -> None:
    print(f"hoge: {x}-{y}/{m}-{n}")


# log_func関数の戻り値を実行
log_hoge = log_func(hoge)
log_hoge(10, 37, m="ほげ", n="ぴょ")
