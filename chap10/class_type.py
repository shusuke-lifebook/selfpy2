from typing import ClassVar


class MyClazz:
    clz: ClassVar[str] = "Person"
    ins1: str = "Instance1"

    def __init__(self, ins2: int) -> None:
        self.ins2 = ins2


if __name__ == "__main__":
    p = MyClazz(15)
    p.ins1 = 123
    p.ins2 = "TEST"
    MyClazz.clz = 10
    p.clz = "Foo"
