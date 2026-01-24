with open("./chap07/input.png", "rb") as reader, open(
    "./chap07/output.png", "wb"
) as writer:
    while d := reader.read(1):
        writer.write(d)
