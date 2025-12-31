flag = False

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result > 50:
            # break時にフラグにTrueに
            flag = True
            break
        print(result, end=" ")
    print()
    # フラグがTrueなら外側もbreak
    if flag:
        break
