import math
from queue import PriorityQueue
from pprint import pprint
f = open("Day8\data.txt")

g = {}
points = []
pq = PriorityQueue()

def getDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

for line in f.readlines():
    a, b, c = map(int, line.strip().split(","))
    points.append((a, b, c))

for i in range(len(points)):
    for j in range(i+1, len(points)):
        tup = (getDistance(points[i], points[j]), i, j)
        pq.put(tup)

while pq.qsize() > 0:
    dist, p1_i, p2_i = pq.get()
    if (p1_i not in g or p2_i not in g) or p1_i not in g[p2_i]:
        g.setdefault(p1_i, set()).add(p2_i)
        g.setdefault(p2_i, set()).add(p1_i)
        if len(g[p1_i]) > len(g[p2_i]):
            g[p1_i].update(g[p2_i])
            g[p2_i] = g[p1_i]
        else:
            g[p2_i].update(g[p1_i])
            g[p1_i] = g[p2_i]
        for k in g[p1_i]:
            g[k] = g[p1_i]
        
    if len(g[p1_i]) == len(points):
        print(points[p1_i], points[p2_i])
        print(points[p1_i][0] * points[p2_i][0])
        break

print("end")