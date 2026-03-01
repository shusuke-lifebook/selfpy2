def hoge() -> str:
    try:
        return "Hoge"
    finally:
        print("**Finally**")


print("Start")
print(hoge())
print("End")
