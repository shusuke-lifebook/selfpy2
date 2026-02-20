import asyncio
import time

from coro import heavy


async def main() -> None:
    t1 = asyncio.create_task(heavy("hoge", 2))
    t2 = asyncio.create_task(heavy("bar", 5))
    t3 = asyncio.create_task(heavy("piyo", 1))
    print(await t1)
    print(await t2)
    print(await t3)


start = time.time()
# コルーチンmainを実行
asyncio.run(main())
end = time.time()
print(f"Process Time: {end - start}")
