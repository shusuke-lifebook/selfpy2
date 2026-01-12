from datetime import date, datetime, time, timedelta, timezone

d = date(2024, 12, 4)
t = time(15, 35, 58, 469)
tz = timezone(timedelta(hours=9))
print(datetime.combine(d, t, tz))
