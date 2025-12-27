import math

print(math.isclose(0.2 * 3, 0.6))
print(math.isclose(0.1, 0.1001, rel_tol=0.0001))
print(math.isclose(0.1, 0.1001, rel_tol=0.001))
