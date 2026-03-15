from enum import Enum


class Season(Enum):
    SPRING = ("春", 3, 5)
    SUMMER = ("夏", 6, 8)
    AUTUMN = ("秋", 9, 11)
    WINTER = ("冬", 12, 2)

    # 初期化メソッド
    def __init__(self, jpname: str, start: int, end: int) -> None:
        self.jpname = jpname
        self.start = start
        self.end = end

    # 季節の情報を返す
    @property
    def message(self) -> str:
        return f"{self.jpname}は{self.start}～{self.end}月です。"


print(Season.SUMMER.start)
print(Season.SUMMER.message)
