from typing import Any


class MyInfo:
    # 属性の格納ための__data(辞書)を準備
    def __init__(self) -> None:
        super().__setattr__("__data", {})

    # 指定された属性を__dataから取得
    def __getattr__(self, name: str) -> Any:
        try:
            return super().__getattribute__("__data")[name]
        except KeyError as ex:
            return None

    # 指定された属性を__dataに格納
    def __setattr__(self, name: str, value: Any) -> None:
        super().__getattribute__("__data")[name] = value


if __name__ == "__main__":
    i = MyInfo()
    i.score = 58
    i.hobby = "卓球"
    print(i.hobby)
    print(i.__dict__)
