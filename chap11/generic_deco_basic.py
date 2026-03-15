from collections.abc import Callable


def log_func[**P, R](func: Callable[P, R]) -> Callable[P, R]:

    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print("----------")
        print(f"Name: {func.__name__}")
        print(f"Args: {args}")
        print(f"Keywds: {kwargs}")
        print("----------")
        return func(*args, **kwargs)

    return inner


@log_func
def hoge(x: int, y: int, m: str = "bar", n: str = "piyo") -> None:
    print(f"hoge: {x} - {y} / {m} - {n}")


hoge(15, "37", m="ほげ", n="ぴよ")
