def concatenate(*args: str) -> str:
    result = args[0]
    result += "・".join(args[2:])
    return result + args[1]


print(concatenate("［", "］", "鈴木", "エルメシア", "富士子"))
