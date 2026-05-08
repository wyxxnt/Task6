def read_chunks(filename, size=512):
    f = open(filename, "r")
    while True:
        data = f.read(size)
        if data == "":
            break
        yield data
    f.close()
