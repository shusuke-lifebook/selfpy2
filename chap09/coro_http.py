import asyncio
import time

from aiohttp import ClientSession


# 指定したアドレスからコンテンツを取得する
async def get_content(session: ClientSession, url: str) -> str:
    print(f"start {url}")
    async with session.get(url) as response:
        text = await response.text()
        print(f"end {url}")
        return text[:100]


async def main() -> tuple[str, ...]:
    # 通信クライアントを生成
    async with ClientSession() as session:
        result = await asyncio.gather(
            get_content(session, "https://codezine.jp"),
            get_content(session, "https://wings.msn.to"),
            get_content(session, "https://www.web-deli.com"),
        )
        return result


start = time.time()
result = asyncio.run(main())
end = time.time()
print(result)
print(f"Process Time: {end - start}")
