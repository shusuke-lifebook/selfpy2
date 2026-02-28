class Parent:
    pass


class Child(Parent):
    pass


if __name__ == "__main__":
    c = Child()
    match c:
        case Parent():
            print("Parent")
        case Child():
            print("Child")
