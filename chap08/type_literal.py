from datetime import datetime
from typing import Literal


def now(type: Literal["datetime", "date", "time"]) -> str:
    dic = {"datetime": "%c", "date": "%x", "time": "%X"}
    dt = datetime.now()
    return dt.strftime(dic[type])


print(now("datetime"))
# print(now("dat")) # 型違反警告
