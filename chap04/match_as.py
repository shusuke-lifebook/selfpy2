lang = ["Python", "Guido van Rossum", 1991]

match lang:
    case [("Python" | "Ruby") as lang, author, created]:
        print(f"{lang}は{author}によって、{created}年に作られました。")
    case [("Java" | "JavaScript") as lang, company]:
        print(f"{lang}は{company}が開発しました。")
