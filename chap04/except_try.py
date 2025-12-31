try:
    num = input("数字を入力してください：")
    print("2倍すると...", float(num) * 2)
except ValueError as ex:
    print("エラーが発生： ", ex)
