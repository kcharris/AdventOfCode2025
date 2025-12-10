"""
For this problem, I could test whether any point inside the shape is to the left or right of any line in a clockwise rotation, or if a point next to a line is another line.
I would only need to check if a point I'm following hits one of these points in a hash. It would be 10^5 dist * 250 segments, or 10**8.
The points i'm following would be tracing lines of the rectangle sides.
"""
f = open("Day9\data.txt")

points = []
for line in f.readlines():
    points.append(list(map(int, line.strip().split(","))))
points.extend(points[:2])
print(len(points))

def getArea(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2+1) * abs(y1-y2+1)

# return -1 if a point is to the left of a line or 1 if it's to the right.
def getD(v1, v2, p):
    x1, y1 = v1
    x2, y2 = v2
    xp, yp = p
    val = (x2 - x1)*(yp - y1) - (xp - x1)*(y2 - y1)
    return -1 if val < 0 else 1

# This is only for concave polygons.
def isPointInsidePolygon(p, poly):
    d = getD(poly[0], poly[1], p)
    for i in range(1, len(poly)-1):
        d2 = getD(poly[i], poly[i+1], p)
        if d2 != d:
            return False
    return True

res = 0
# solution code

# for i in range(len(points)-3):
#     r1, r2, r3 = points[i:i+3]
#     x1, y1 = r1
#     x2, y2 = r2
#     x3, y3 = r3
#     p = (x1 + x3 - x2, y1 + y3 - y2)
#     if isPointInsidePolygon(p, points):
#         res = max(res, getArea(r1, r3))

print(res)