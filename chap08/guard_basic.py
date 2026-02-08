def process(value: str | int) -> str | int:
    if isinstance(value, str):
        return value.upper()
    else:
        return value + 10


print(process("abc"))
print(process(100))
