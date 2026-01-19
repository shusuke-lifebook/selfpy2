d = {"apple": "りんご", "orange": "みかん", "melon": "メロン"}
d["apple"] = "林檎"
d["strawberry"] = "いちご"
print(d.setdefault("apple", "〇"))
print(d.setdefault("watermelon", "〇"))
print(d)
