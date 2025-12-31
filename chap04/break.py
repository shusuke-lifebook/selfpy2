sum = 0

for i in range(1, 101):
    sum += i
    if sum > 1000:
        break

print(f"合計が10000を超えるのは、1～{i}を加算したときです。")
