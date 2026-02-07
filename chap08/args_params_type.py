from typing import NotRequired, TypedDict, Unpack


# title, size, fullキーを持つ型付き辞書を準備
class KeywordArgs(TypedDict):
    title: str
    size: int
    full: NotRequired[bool]


def hoge(**kwargs: Unpack[KeywordArgs]) -> None:
    print(kwargs)


hoge(title="Python入門", size=100, full=True)
hoge(title="Hello", size=100)
# hoge(title="Hello", full=True) # エラー
# hoge(title="Hello", size="100px") # エラー
# hoge(title="Hello", size=100, none='none') # エラー
