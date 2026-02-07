# arg1は位置引数であること
def my_func(arg1: int, /, arg2: int = 0, arg3: int = 0) -> None:
    pass


# my_func(arg1=10, arg2=20)  # エラー さらに 1 つの位置引数が必要です
my_func(10, arg2=20)  # OK
