data = "グローバル"


def check_scope() -> str:
    global data
    data = "ローカル"
    return data


print(check_scope())
print(data)
