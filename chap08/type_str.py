from typing import LiteralString


def build_sql(keyword: LiteralString) -> str:
    return f'SELECT * FROM items WHERE keyword = "{keyword}"'


print(build_sql("Python"))

# key = input()
# print(build_sql(key)) # 型 "str" の引数を、関数 "build_sql" の型 "LiteralString" のパラメーター "keyword" に割り当てることはできません。
