try:
    raise ExceptionGroup(
        "Multi Exception!!",
        [ValueError("Value is invalid..."), TypeError("Type is unknown.")],
    )
except* ValueError as e:
    print(f"Value: {repr(e)}")
except* TypeError as e:
    print(f"Type: {repr(e)}")
except* IndexError as e:
    print(f"Index: {repr(e)}")
