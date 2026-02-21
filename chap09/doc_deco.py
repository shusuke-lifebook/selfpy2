from collections.abc import Callable
from functools import wraps
from typing import Any


def log_func(func: Callable[..., Any]) -> Callable[..., Any]:
    """関数情報を出力するデコレーター"""

    @wraps(func)
    def inner(*args, **keywds):
        """関数情報を出力"""
        print("----------")
        print(f"Name: {func.__name__}")
        print(f"Args: {args}")
        print(f"Keywds: {keywds}")
        print("----------")
        return func(*args, **keywds)

    return inner


@log_func
def hoge(x: int, y: int, m: str = "bar", n: str = "piyo") -> None:
    """デコレーター確認のための関数"""
    print(f"hoge: {x}-{y}/{m}-{n}")


if __name__ == "__main__":
    print(hoge.__name__)
    print(hoge.__doc__)
