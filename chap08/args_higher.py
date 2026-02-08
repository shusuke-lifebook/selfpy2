from collections.abc import Callable
from typing import Any


# 高階関数walk_list関数を定義
def walk_list(data: list[Any], func: Callable[[Any, int], None]) -> None:
    # リストの内容を順に処理
    for key, value in enumerate(data):
        # func経由で指定の関数を呼び出し
        func(value, key)


# リストを処理するためのユーザー定義関数
def show_item(value: Any, key: int) -> None:
    print(key, ":", value)


data = [105, 53, 27, 87, 33]
walk_list(data, show_item)
