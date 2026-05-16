import os
from stream import read_lines

f = open("data.txt", "w")
i = 1
while i <= 10000:
    f.write(str(i) + "\n")
    i = i + 1
f.close()

print("file size:", os.path.getsize("data.txt"), "bytes")

total = 0
count = 0
for line in read_lines("data.txt"):
    num = int(line)
    if num % 2 == 0:
        total = total + num
        count = count + 1

print("even numbers:", count)
print("sum of even:", total)
print("average:", total / count)

os.remove("data.txt")
