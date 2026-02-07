msg = "before"


def my_func(param: str = msg) -> None:
    print(param)


msg = "after"
my_func()
