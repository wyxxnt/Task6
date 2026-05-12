def read_chunks(filename, size=512):
    f = open(filename, "r")
    while True:
        data = f.read(size)
        if data == "":
            break
        yield data
    f.close()
def read_lines(filename, size=512):
    buf = ""
    for chunk in read_chunks(filename, size):
        buf = buf + chunk
        parts = buf.split("\n")
        buf = parts[len(parts) - 1]
        i = 0
        while i < len(parts) - 1:
            yield parts[i]
            i = i + 1
    if buf != "":
        yield buf
