import random

gen = (random.random() for i in range(100))

for num in gen:
    print(num)
