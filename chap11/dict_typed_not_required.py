from typing import NotRequired, TypedDict


class PersonDict(TypedDict):
    name: str
    age: int
    married: NotRequired[bool]


p1: PersonDict = {"name": "Yamada", "age": 25}
# p2: PersonDict = {"name": "Yamada", "age": 25, "married": True, "gender": "male"}
