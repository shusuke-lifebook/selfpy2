from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

print(datetime.today())
print(date.today())
print(datetime.now())
print(datetime.now(timezone(timedelta(hours=9))))
print(datetime.now(ZoneInfo("Asia/Tokyo")))
print(datetime.now(timezone.utc))
