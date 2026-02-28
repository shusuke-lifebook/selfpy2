class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname


if __name__ == "__main__":
    p = Person("太郎", "鈴木")
    match p:
        case Person(firstname=fn, lastname="山田"):
            print(f"山田一族の{fn}です。")
        case Person(firstname=fn, lastname="鈴木"):
            print(f"氏は鈴木、名は{fn}です。")
