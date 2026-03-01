file = None
try:
    file = open("./chap11/sample.txt", "r", encoding="utf-8")
    data = file.read()
    print(data)
finally:
    # ファイルが存在する場合、これを閉じる
    if file:
        file.close()
