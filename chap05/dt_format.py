import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, "ja_JP.UTF-8")

dt = datetime(2024, 12, 4, 15, 35, 58, 469)
print(dt)
print(dt.strftime("%c"))
print(dt.strftime("%x"))
print(dt.strftime("%X"))
print(dt.strftime("%Y年 %m月 %d日 (%a) %I時 %M分"))
