from datetime import datetime, timezone

dt = datetime.now(timezone.utc)
print(dt)
print(dt.date())
print(dt.time())
print(dt.timetz())
print(dt.timestamp())
print(dt.toordinal())
print(dt.weekday())
print(dt.isoweekday())
print(dt.isocalendar())
