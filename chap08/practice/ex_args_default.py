def get_square(base: float = 1.0, height: float = 1.0) -> float:
    return base * height


print(f"平行四辺形の面積は{get_square()}です。")
print(f"平行四辺形の面積は{get_square(10)}です。")
print(f"平行四辺形の面積は{get_square(10.5, 5)}です。")
