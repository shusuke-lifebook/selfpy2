from datetime import datetime

dt1 = datetime(2024, 12, 4, 15, 35, 58, 469)
dt2 = dt1.replace(day=25, minute=59)
print(dt1)
print(dt2)
