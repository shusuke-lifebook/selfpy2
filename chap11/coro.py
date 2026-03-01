import asyncio
import random
from typing import Any


async def heavy_raise(clazz: Any) -> str:
    name = clazz.__name__
    print(f"{name} start...")
    rand = random.randint(0, 5)
    await asyncio.sleep(rand)
    # 乱数が1より大きい場合、渡された例外をスロー
    if rand > 1:
        raise clazz(f"{name}: {rand}sec")
    print(f"{name} end...")
    return f"{name}: {rand}"
