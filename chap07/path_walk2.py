import os

for path, dirs, files in os.walk("./chap07/doc"):
    # 配下のファイルだけを列挙
    for f in files:
        # 拡張子「.txt」ものだけを表示
        if f.endswith(".txt"):
            print(os.path.join(path, f))
