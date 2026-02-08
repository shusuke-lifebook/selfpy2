def average(*values: float) -> float:
    result = 0
    for value in values:
        result += value
    return result / len(values)


print(average(5, 7, 8, 2, 1, 15))
