from types import TracebackType
from typing import Self


class MyContext:
    # コンテキスの作成
    def __enter__(self) -> Self:
        print("**Enter**")
        return self

    # コンテキストの開放
    def __exit__(self, t: type, value: Exception, tb: TracebackType) -> bool:
        # 例外の有無を判定
        if t is None:
            print("**Exit**")
        else:
            print(f"**{value}**")
            return True

    def hoge(self) -> None:
        print("Hoge")


with MyContext() as c:
    print("With Start")
    c.hoge()
