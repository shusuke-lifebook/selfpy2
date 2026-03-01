try:
    raise Exception("例外が発生")
except Exception as ex:
    print(ex.args[0])
finally:
    print("**finally**")
