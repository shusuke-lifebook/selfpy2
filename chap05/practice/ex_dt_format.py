import locale
from datetime import datetime, timedelta, timezone

locale.setlocale(locale.LC_ALL, "ja_JP.UTF-8")
dt = datetime(2024, 12, 4, 11, 37, 20, 0, timezone(timedelta(hours=9)))
print(dt.strftime("%Y年 %m月 %d日 %I時"))
