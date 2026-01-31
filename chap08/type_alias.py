from datetime import datetime
from typing import Literal

type UserInfo = tuple[str, Literal["male", "female"], datetime, bool]
p: UserInfo = ("Yamada, Yoshihiro", "male", datetime(2007, 6, 25), True)
