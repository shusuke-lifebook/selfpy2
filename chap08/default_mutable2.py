def my_func(value: int, data: list[int] | None = None) -> list[int]:
    if data is None:
        data = []
    data.append(value)
    return data


print(my_func(13))
print(my_func(108))
