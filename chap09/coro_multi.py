import asyncio
import time

from coro import heavy


async def main() -> None:
    print(await heavy("hoge", 2))
    print(await heavy("bar", 5))
    print(await heavy("piyo", 1))


start = time.time()
# コルーチンmainを実行
asyncio.run(main())
end = time.time()
print(f"Process Time: {end - start}")
