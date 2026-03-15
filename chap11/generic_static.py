class Util:
    @staticmethod
    def get_elements_except[T](es: list[T], value: T):
        return [e for e in es if e != value]


print(Util.get_elements_except([10, 12, 11, 10, 15], 10))
