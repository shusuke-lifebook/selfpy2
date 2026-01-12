from datetime import date, datetime, time, timedelta, timezone

print(datetime(2024, 12, 4, 15, 35, 58, 469))
print(datetime(2024, 12, 4, 15, 35, 58, 469, timezone(timedelta(hours=9))))
print(date(2024, 12, 4))
print(time(15, 35, 58, 469))
print(time(15, 35, 58, 469, timezone(timedelta(hours=9))))
print(datetime(2024, 13, 4, 15, 35, 58, 469))
