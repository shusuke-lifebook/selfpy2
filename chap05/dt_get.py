from datetime import datetime, timezone

dt = datetime.now(timezone.utc)

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.tzinfo)
