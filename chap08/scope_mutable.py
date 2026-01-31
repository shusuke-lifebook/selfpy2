def param_update(data: list[int]) -> list[int]:
    data[0] = 55
    return data


data = [2, 4, 6]
print(param_update(data)[0])
print(data[0])
