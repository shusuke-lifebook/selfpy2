lang = ["Python", "Guido van Rossum", 1991]

match lang:
    case [("Python" | "Ruby"), author, created]:
        print(f"{author}によって、{created}年に作られました。")
    case [("Java" | "JavaScript"), company]:
        print(f"{company}が開発しました。")
