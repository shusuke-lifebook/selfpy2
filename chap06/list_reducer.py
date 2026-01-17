import functools

data = [2, 4, 6, 8]
multi = functools.reduce(lambda result, x: result * x, data)
print(multi)
