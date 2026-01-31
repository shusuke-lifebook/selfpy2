num = 3


def check_scope() -> int:
    print(num)  # 結果エラー
    num = 108
    return num


print(check_scope())
