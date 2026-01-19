from collections import defaultdict

data = ["太郎", "花子", "次郎", "太郎", "太郎", "太郎", "花子"]
result = defaultdict(int)

for key in data:
    result[key] += 1

print(result)
