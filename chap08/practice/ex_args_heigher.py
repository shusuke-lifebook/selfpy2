from collections.abc import Callable


def process_number(func: Callable[[int], int], *nums: int) -> list[int]:
    result = []
    for num in nums:
        result.append(func(num))
    return result


data = process_number(lambda num: num**2, 5, 3, 6)
print(data)
