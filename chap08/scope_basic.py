data1 = "グローバル"


def check_scope():
    data2 = "ローカル"
    return data1


print(check_scope())
# print(data2)  # NameError: name 'data2' is not defined
