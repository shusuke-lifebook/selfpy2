import asyncio
import time

from coro import heavy


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as group:
            t1 = group.create_task(heavy("hoge", 2))
            t2 = group.create_task(heavy("bar", 5))
            t3 = group.create_task(heavy("piyo", 1))
    except Exception as e:
        print(e)
    print([t1._state, t2._state, t3._state])
    # print([t1.result(), t2.result(), t3.result()])


start = time.time()
# コルーチンmainを実行
asyncio.run(main())
end = time.time()
print(f"Process Time: {end - start}")
