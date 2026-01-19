import re

msg = "電話番号は080-111-9999です。"
# 正規表現の準備
ptn = re.compile(r"(\d{2,4})-(\d{2,4})-(\d{4})")
# 文字列を検索&結果を表示
if result := ptn.search(msg):
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
else:
    print("見つかりませんでした。")
