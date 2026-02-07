def total_products(init: int, *values: int):
    result = init
    for value in values:
        result *= value
    return result


print(total_products())  # エラー　パラメーター "init" に引数がありません
