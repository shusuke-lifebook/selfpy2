lang = ["Python", "Guido van Rossum", 1991, "3.13"]

match lang:
    case ["Python", *info, version]:
        print(
            f"Pythonは{info[0]}によって、{info[1]}年に作られました。最新バージョンは{version}です。"
        )
    case ["Ruby", *info, version]:
        print(
            f"Rubyは{info[0]}によって、{info[1]}年に作られました。最新バージョンは{version}です。"
        )
