def total_products(*values: int) -> int:
    result = 1
    for value in values:
        result *= value
    return result


print(total_products(12, 15, -1))
print(total_products(5, 7, 8, 2, 1, 15))
