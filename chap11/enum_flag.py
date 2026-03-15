from enum import Flag, auto


class FontStyle(Flag):
    BOLD = auto()
    ITALIC = auto()
    UNDERLINE = auto()
    STRIKETHROUGH = auto()


for style in FontStyle:
    print(f"{style.name}: {style.value} (={bin(style.value)})")
