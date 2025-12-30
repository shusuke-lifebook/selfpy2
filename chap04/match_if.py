obj = -123

match obj:
    case int() if obj >= 15:
        print("15以上の整数です。")
    case int():
        print("整数です。")
    case str() if len(obj) < 10:
        print("10文字未満の文字列です。")
    case _:
        print("意図しない型です。")
