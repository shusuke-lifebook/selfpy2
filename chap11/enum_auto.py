from enum import Enum, auto


class Season(Enum):
    SPRING = auto()
    SUMMER = auto()
    AUTUMN = auto()
    WINTER = auto()


print(Season.SUMMER.value)
