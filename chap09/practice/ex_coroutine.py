import asyncio
import time


async def heavy(name: str, sec: int) -> str:
    print(f"{name} start...")
    await asyncio.sleep(sec)
    print(f"{name} end...")
    return f"{name}:{sec} sec"


async def main() -> None:
    print(await asyncio.gather(heavy("hoge", 2), heavy("bar", 5), heavy("piyo", 1)))


start = time.time()
asyncio.run(main())
end = time.time()
print(f"Process Time: {end - start}")
