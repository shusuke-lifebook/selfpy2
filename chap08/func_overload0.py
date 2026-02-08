def process(value: int | str) -> int | str:
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return len(value)
    else:
        raise TypeError("不正な型です。")


result1: str = process(123)  # type: ignore
result2: int = process("hoge")  # type: ignore
