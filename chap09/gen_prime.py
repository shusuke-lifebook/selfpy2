import math
from collections.abc import Generator


# 素数を求めるジェネレーター
def get_primes() -> Generator[int]:
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# 引数valueが素数であるかを判定する
def is_prime(value: int) -> bool:
    result = True
    # 2 ～ sqrt(value)でvalue替わり消えれ宇(余りが0)ものがあるか
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result


# 素数を順に出力する
for prime in get_primes():
    print(prime)
    # 素数が100を超えたところで、終了
    if prime > 100:
        break
