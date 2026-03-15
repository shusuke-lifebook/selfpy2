from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


for season in Season:
    print(f"{season.name}: {season.value}")

print(Season(1))
print(Season["SPRING"])
print(1 in Season)
print(len(Season))
print(list(reversed(Season)))
