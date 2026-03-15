from collections import defaultdict


class GenericConstraint[T: dict]:
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> tuple:
        return self.value.popitem()


if __name__ == "__main__":
    GenericConstraint({"a": 1}).get()
    GenericConstraint(defaultdict(int)).get()
    # GenericConstraint(13).get()
