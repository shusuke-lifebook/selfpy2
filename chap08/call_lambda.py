from collections.abc import Callable
from typing import Any


# 高階関数
def walk_list(data: list[Any], func: Callable[[Any, int], None]) -> None:
    for key, value in enumerate(data):
        func(value, key)


data = [105, 53, 27, 87, 33]
walk_list(data, lambda value, key: print(key, ":", value))
