# arg2,3はキーワードは引数であること
def my_func(arg1: int, *, arg2: int = 0, arg3: int = 0) -> None:
    pass


# my_func(1, 2, 3)  # エラー　1 個の位置引数が必要です
my_func(1, arg2=2, arg3=3)  # OK
