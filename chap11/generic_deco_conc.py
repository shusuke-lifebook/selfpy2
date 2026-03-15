from collections.abc import Callable
from typing import Concatenate


def prefix[**P, R](func: Callable[Concatenate[str, P], R]) -> Callable[P, R]:

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func("decorated", *args, **kwargs)

    return wrapper


@prefix
def hoge(prefix: str, x: int, y: int) -> None:
    print(f"{prefix}: {x + y}")


if __name__ == "__main__":
    hoge(10, 20)
