def create_dict(**kwargs: str | int) -> dict[str, str | int]:
    result = dict()
    for key, value in kwargs.items():
        result[key] = value
    return result


d = create_dict(name="山田太郎", age=30, sex="male")
print(d)
