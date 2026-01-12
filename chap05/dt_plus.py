from datetime import datetime, timedelta

dt = datetime(2024, 12, 4, 15, 35, 58, 469)
dt_p = dt + timedelta(days=15, hours=5)
dt_m = dt - timedelta(weeks=3)

print(dt)
print(dt_p)
print(dt_m)
