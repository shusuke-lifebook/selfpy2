from enum import Enum

Season = Enum("Season", "SPRING SUMMER AUTUMN WINTER")
# Season = Enum('Season', (('SPRING', 10), ('SUMMER', 20),
#                          ('AUTUMN', 30), ('WINTER', 40)))
# Season = Enum('Season', {
#     'SPRING': 1, 'SUMMER': 2, 'AUTUMN': 3, 'WINTER': 4})

for season in Season:
    print(f"{season.name}: {season.value}")
