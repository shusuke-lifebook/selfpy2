import asyncio

from coro import heavy_raise


async def main() -> None:
    try:
        # TaskGroupに3個のタスクを登録
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(heavy_raise(ValueError))
            t2 = tg.create_task(heavy_raise(TypeError))
            t3 = tg.create_task(heavy_raise(RuntimeError))
        print([t1.result(), t2.result(), t3.result()])
    except* TypeError as e:
        print(f"Type: {repr(e)}")
    except* ValueError as e:
        print(f"Value: {repr(e)}")
    except* RuntimeError as e:
        print(f"Runtime: {repr(e)}")


asyncio.run(main())
