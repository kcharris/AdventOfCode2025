f = open("Day1\data.txt")
res = 0
curr = 50
for line in f.readlines():
    direction = 1
    letter, num = line[0], int(line[1:])
    if letter == "L":
        direction = -1

    for i in range(num):
        curr = (curr + direction) % 100
        if curr == 0:
            res += 1

print(res)