try:
    raise ExceptionGroup(
        "Multi Exception!!",
        [ValueError("value is invalid..."), TypeError("Type is unknown.")],
    )
except ValueError as e:
    print(f"Value: {e.args[0]}")
except ExceptionGroup as e:
    print(f"Group: {e.args[0]}")
