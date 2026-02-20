import asyncio
import random

# 擬似的な「重い」処理


async def heavy(name: str, sec: int) -> str:
    print(f"{name} start...")
    # ダミーの重い処理(secだけ処理を休止)
    await asyncio.sleep(sec)
    # 50 % の確率で例外を発生
    if random.randint(0, 1) == 0:
        raise ValueError(f"{name} occurs error.")
    print(f"{name} end...")
    return f"{name}:{sec} sec"
