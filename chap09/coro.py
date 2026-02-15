import asyncio

# 擬似的な「重い」処理


async def heavy(name: str, sec: int) -> str:
    print(f"{name} start...")
    # ダミーの重い処理(secだけ処理を休止)
    await asyncio.sleep(sec)
    print(f"{name} end...")
    return f"{name}:{sec} sec"
