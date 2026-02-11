from collections.abc import Callable
from typing import Any


# デコレーターの引数を受け取る
def log_func(
    details: bool = True,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

    # 修飾すべき関数を受け取る
    def outer(func: Callable[..., Any]) -> Callable[..., Any]:
        # 本来の関数に渡すべき引数を受け取る
        def inner(*args, **keywds):
            print("----------")
            print(f"Name: {func.__name__}")
            if details:
                print(f"Args: {args}")
                print(f"Keywds: {keywds}")
            print("----------")
            return func(*args, **keywds)

        return inner

    return outer


@log_func(details=False)
def hoge(x: int, y: int, m: str = "bar", n: str = "piyo") -> None:
    print(f"hoge: {x}-{y}/{m}-{n}")


hoge(15, 37, m="ほげ", n="ぴょ")
