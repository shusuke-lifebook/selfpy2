import keyword

id1 = "tiff"
id2 = "if-else"
id3 = "if"

print(id1.isidentifier())
print(id2.isidentifier())
print(keyword.iskeyword(id1))
print(keyword.iskeyword(id3))
