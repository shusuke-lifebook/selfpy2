from typing import TypedDict


class PersonDict(TypedDict):
    name: str
    age: int
    married: bool


# PersonDict = TypedDict(
#     'PersonDict', {'name': str, 'age': int, 'married': bool})

person: PersonDict = {"name": "Yamada", "age": 25, "married": False}
# person: PersonDict = {"name": "Yamada", "age": "25歳", "married": "未婚"}

# p1: PersonDict = {'name': 'Yamada', 'age': 25}
# p2: PersonDict = {'name': 'Yamada', 'age': 25, 'married': True, 'gender': 'male'}
