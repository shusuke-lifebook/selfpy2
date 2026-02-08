from warnings import deprecated


@deprecated("代わりにget_area関数を利用すべきです。")
def get_triangle(base: float = 5, height: float = 1) -> float:
    return base * height / 2


print(get_triangle(10, 5))
