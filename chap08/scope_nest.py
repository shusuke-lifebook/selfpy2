data = "global"


def outer() -> str:
    data = "outer"

    def inner() -> str:
        data = "inner"
        return data

    return inner()


print(outer())
