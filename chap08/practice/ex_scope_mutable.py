def increment(num: int) -> int:
    num += 10
    return num


def param_update(data: list[int]) -> list[int]:
    data[0] = 100
    return data


num = 100
data = [10, 20, 30]
print(increment(num))
print(num)
print(param_update(data))
print(data)
