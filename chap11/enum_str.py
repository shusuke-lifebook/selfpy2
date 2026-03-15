from enum import StrEnum, auto


# 選択可能なコマンドを準備
class Command(StrEnum):
    ATTACK = auto()
    MAGIC = auto()
    DEFEND = auto()
    ESCAPE = auto()


# ユーザーにコマンド入力を促す
comm = input("次の行動を入力してください：")

# 入力されたコマンドに応じてメッセージを出力
match comm:
    case Command.ATTACK:
        print("攻撃します")
    case Command.MAGIC:
        print("魔法を使います")
    case Command.DEFEND:
        print("防御します")
    case Command.ESCAPE:
        print("逃げます")
    case _:
        print("無効な行動です")
