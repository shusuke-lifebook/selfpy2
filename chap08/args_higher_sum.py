from collections.abc import Callable
from typing import Any


# 高階関数walk_list関数を定義
def walk_list(data: list[Any], func: Callable[[Any, int], None]) -> None:
    for key, value in enumerate(data):
        func(value, key)


result = 0


def calcu_sum(value: float, key: int) -> None:
    global result
    result += value


data = [105, 53, 27, 87, 33]
walk_list(data, calcu_sum)
print(result)
