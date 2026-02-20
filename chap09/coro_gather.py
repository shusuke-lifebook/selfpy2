import asyncio
import time

from coro import heavy


async def main() -> None:
    print(
        await asyncio.gather(
            heavy("hoge", 2), heavy("bar", 5), heavy("piyo", 1), return_exceptions=True
        )
    )


start = time.time()
# コルーチンmainを実行
asyncio.run(main())
end = time.time()
print(f"Process Time: {end - start}")
