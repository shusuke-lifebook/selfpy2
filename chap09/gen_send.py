from collections.abc import Generator


def gen_com() -> Generator[str, str]:
    while True:
        # ユーザー入力を要求
        n = yield input("名前を教えてください：")
        # sendメソッドからの値でメッセージを生成
        yield f"こんにちは、{n}さん！"


gen = gen_com()
for name in gen:
    # ジュネレーターからの戻り値(入力値)を再送出
    res = gen.send(name.upper())
    # ジュネレーターから戻り値(あいさつメッセージ)を表示
    print(res)
