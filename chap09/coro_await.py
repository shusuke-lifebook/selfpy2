import asyncio
import time

import requests


# 指定のURLにリクエストし結果を取得
async def get_content(url) -> str:
    print(f"start {url}")
    res = requests.request("get", url)
    print(f"end {url}")
    return res.text[:100]


# 非同期処理のエントリーポイント
async def main() -> tuple[str, ...]:
    return await asyncio.gather(
        get_content("https://codezine.jp"),
        get_content("https://wings.msn.to"),
        get_content("https://www.web-deli.com"),
    )


start = time.time()
result = asyncio.run(main())
end = time.time()
print(result)
print(f"Process Time: {end - start}")
