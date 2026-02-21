from collections.abc import Callable
from datetime import datetime
from time import sleep
from typing import Any


def time_deco(func: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args, **keywds):
        print(f"{func.__name__} Start: {datetime.now()} ")
        result = func(*args, **keywds)
        print(f"{func.__name__} End: {datetime.now()} ")
        return result

    return inner


@time_deco
def hoge() -> None:
    sleep(3)
    print("hoge is running.")


hoge()
