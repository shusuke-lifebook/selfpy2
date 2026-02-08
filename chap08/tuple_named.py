from typing import NamedTuple

# MaxMin型の名前付きタプルを定義
MaxMin = NamedTuple("MaxMin", [("max", float), ("min", float)])


def get_max_min(*args: float) -> MaxMin:
    return MaxMin(max(args), min(args))


result = get_max_min(15, 7.5, 108, -10)
print(result.max)
print(result.min)
print(result[0])
