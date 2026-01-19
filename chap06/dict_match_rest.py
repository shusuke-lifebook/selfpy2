# 書籍情報を表す辞書
book = {
    "isbn": "978-4-7981-8055-7",
    "title": "独習 ASP.NET Core",
    "publisher": "翔泳社",
    "price": 4290,
    "page": 672,
}

match book:
    case {"isbn": _, "title": title, **info}:
        print(f"{title} ({info})")
    case {"url": url, "title": title}:
        print(f"{title} ({url})")
