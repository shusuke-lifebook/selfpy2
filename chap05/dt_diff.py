from datetime import datetime

dt1 = datetime(2024, 11, 30, 4, 46, 14, 123)
dt2 = datetime(2025, 12, 4, 15, 35, 58, 469)
delta = dt2 - dt1
print(delta)
print(delta.days)
print(delta.seconds)
