import asyncio

from coro import heavy

result = asyncio.run(heavy("hoge", 2))
print(result)
