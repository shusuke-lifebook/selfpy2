from datetime import datetime

dt1 = datetime.strptime("2024/8/5 11:37:25", "%Y/%m/%d %H:%M:%S")
print(dt1)
dt2 = datetime.fromisoformat("2024-08-05T11:37:25+09:00")
print(dt2)
dt3 = datetime.fromisoformat("2024-08-05T11:37:25.145Z")
print(dt3)
