import re

msg = "仕事用はwings@example.comです。プライベート用はYAMA@example.comです。"
ptn = re.compile(
    r"""[a-z0-9.!#$%&'*+/=?^_{|}~-]+ # local
                     @                            # delimiter
                     [a-z0-9-]+(\.[a-z0-9-]+)*    # domain """,
    re.IGNORECASE | re.VERBOSE,
)

results = ptn.finditer(msg)
for result in results:
    print(result.group())
