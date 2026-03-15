from typing import ReadOnly, TypedDict


class PersonDict(TypedDict):
    name: ReadOnly[str]
    age: int
    married: bool


person: PersonDict = {"name": "Yamada", "age": 25, "married": False}
# person["name"] = "Suzuki"
