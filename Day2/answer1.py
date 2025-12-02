f = open("Day2\data.txt")

data = f.readline().split(",")

res = 0
for s in data:
    a, b = [int(x) for x in s.split("-")]

    for i in range(a, b+1):
        sn = str(i)
        if len(sn) & 1 == 1:
            continue
        if sn[:len(sn)//2] == sn[len(sn)//2:]:
            res += i

print(res)