f = open("Day9\data.txt")

points = []
for line in f.readlines():
    points.append(list(map(int, line.strip().split(","))))

def getArea(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1-x2+1) * abs(y1-y2+1)

res = 0
for p1 in points:
    for p2 in points:
        res = max(res, getArea(p1, p2))
print(res)