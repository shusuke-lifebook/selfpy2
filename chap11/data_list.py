import dataclasses


@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = 0
    memos: list[str] = dataclasses.field(default_factory=list)


if __name__ == "__main__":
    ms = ["married", "AB"]
    p = Person("太郎", "山田", 58, ms)
    print(p)
    # フィールドで経由したオブジェクトを変更
    p.memos.append("dog")
    print(p)
