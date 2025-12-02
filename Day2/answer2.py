f = open("Day2\data.txt")

data = f.readline().split(",")

res = 0
for s in data:
    a, b = [int(x) for x in s.split("-")]

    for i in range(a, b+1):
        sn = str(i)
        w = 1
        flag = False
        while w <= len(sn) // 2:
            if len(sn) % w == 0:
                pattern = sn[:w]
                flag = True
                for j in range(w, len(sn)-w+1, w):
                    if pattern != sn[j: j+w]:
                        flag = False
                        break
                if flag == True:
                    break
            w += 1
        if flag == True:
            res += i

print(res)