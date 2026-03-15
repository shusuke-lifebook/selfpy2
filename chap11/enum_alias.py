from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    FALL = AUTUMN
    WINTER = 4


print(Season.FALL.name)
print(len(Season))
