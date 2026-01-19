# 書籍情報を表す辞書
book = {
    "isbn": "978-4-7981-8055-7",
    "title": "独習 ASP.NET Core",
    "publisher": "翔泳社",
    "price": 4290,
    "page": 672,
}

# 記事情報を表す辞書
article = {
    "url": "https://codezine.jp/article/corner/1009",
    "title": "「GitHub Copilot」 入門",
    "time": 8,
}

match book:
    case {"isbn": _, "title": title, "publisher": publisher}:
        print(f"{title} ({publisher}刊)")
    case {"url": url, "title": title}:
        print(f"{title} ({url})")
    case _:
        print("コンテンツの種類が不明です。")
