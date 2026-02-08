from typing import overload


@overload
def process(value: int) -> str: ...


@overload
def process(value: str) -> int: ...


def process(value: int | str) -> int | str:
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return len(value)
    else:
        raise TypeError("不正な型です。")


result1: str = process(123)
result2: int = process("hoge")
print(result1, result2)
