obj = -123

match obj:
    case int():
        print(abs(obj))
    case str():
        print(obj[0])
    case _:
        print("意図しない型です。")
