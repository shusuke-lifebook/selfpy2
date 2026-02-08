data = ["こんにちは", "おはよう", "おやすみ"]
keywd = {"sep": ",", "end": "●"}
print(*data, **keywd)  # type: ignore
