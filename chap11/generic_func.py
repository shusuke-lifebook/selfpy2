def get_elements_except[T](es: list[T], value: T) -> list[T]:
    return [e for e in es if e != value]


print(get_elements_except([10, 12, 11, 10, 15], 10))
print(get_elements_except(["hoge", "foo", "bar", "foo"], "foo"))
