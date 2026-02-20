import asyncio
import time

from coro import heavy


async def main() -> None:
    async with asyncio.TaskGroup() as group:
        t1 = group.create_task(heavy("hoge", 2))
        t2 = group.create_task(heavy("bar", 5))
        t3 = group.create_task(heavy("piyo", 1))
    print([t1.result(), t2.result(), t3.result()])


start = time.time()
# コルーチンmainを実行
asyncio.run(main())
end = time.time()
print(f"Process Time: {end - start}")
