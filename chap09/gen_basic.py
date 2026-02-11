from collections.abc import Generator


def my_gen() -> Generator[str]:
    yield "あいうえお"
    yield "かきくけこ"
    yield "さしすせそ"


for value in my_gen():
    print(value)
