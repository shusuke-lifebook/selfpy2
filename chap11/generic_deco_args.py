from collections.abc import Callable


def log_func[**P, R](
    details: bool = True,
) -> Callable[[Callable[P, R]], Callable[P, R]]:

    def outer(func: Callable[P, R]) -> Callable[P, R]:
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            print("----------")
            print(f"Name: {func.__name__}")
            if details:
                print(f"Args: {args}")
                print(f"kwargs: {kwargs}")
            print("----------")
            return func(*args, **kwargs)

        return inner

    return outer


@log_func(details=False)
def hoge(x: int, y: int, m: str = "bar", n: str = "piyo") -> None:
    print(f"hoge: {x}-{y}/{m}-{n}")


hoge(15, 37, m="ほげ", n="ぴよ")
