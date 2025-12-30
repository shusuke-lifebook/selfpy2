lang = ["Python", "Guido van Rossum", 1991]

match lang:
    case ["JavaScrpipt"]:
        print("1個のシーケンス: JavaScript")
    case ["Python"]:
        print("1個のシーケンス: Python")
    case ["Python", "Guido van Rossum"]:
        print("2個のシーケンス")
    case ["Python", "Guido van Rossum", 1991]:
        print("3個のシーケンス")
