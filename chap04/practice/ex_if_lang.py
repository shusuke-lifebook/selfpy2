language = "Python"

match language:
    case "Python" | "Perl" | "Ruby":
        print("インタプリター言語")
    case "C#" | "C++" | "Java":
        print("コンパイル言語")
    case _:
        print("不明")
