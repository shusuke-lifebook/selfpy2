def my_func(value: int, data: list[int] = []) -> list[int]:
    data.append(value)
    return data


print(my_func(13))
print(my_func(108))
