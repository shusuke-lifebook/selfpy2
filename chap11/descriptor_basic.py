from typing import Any


# ディスクリプターの定義
class LogProp:
    # 対象の属性名(name)を設定
    def __init__(self, name: str) -> None:
        self.name = name

    # 属性取得の処理
    def __get__(self, obj: object, t: type) -> Any:
        print(f"{self.name}: get")
        return obj.__dict__[self.name]

    # 属性設定の処理
    def __set__(self, obj: object, value: Any) -> None:
        print(f"{self.name}: set {value}")
        obj.__dict__[self.name] = value


class App:
    # ディスクリプターを定義
    title = LogProp("title")


if __name__ == "__main__":
    app = App()
    app.title = "独習Python"
    print(app.title)
