data = "global"


def outer() -> None:
    data = "outer"

    def inner() -> str:
        # global data
        nonlocal data
        data = "inner"
        return data

    print(inner())
    print(data)


outer()
print(data)
