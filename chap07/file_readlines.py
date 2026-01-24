with open("./chap07/sample.txt", "r", encoding="UTF-8") as file:
    data = file.readlines()

# リストの内容を出力
for line in data:
    print(line, end="")
