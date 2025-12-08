import math
from queue import PriorityQueue
from pprint import pprint
f = open("Day8\data.txt")

g = {}
points = []
pq = PriorityQueue()

def getDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def sameCircuit(p1i, p2i):
    visited = {p1i}
    nodes = [p1i]
    while len(nodes) > 0:
        node = nodes.pop()
        if node == p2i:
            return True
        for next_node in g[node]:
            if next_node not in visited:
                visited.add(next_node)
                nodes.append(next_node)
    return False

for line in f.readlines():
    a, b, c = map(int, line.strip().split(","))
    points.append((a, b, c))

for i in range(len(points)):
    for j in range(i+1, len(points)):
        tup = (getDistance(points[i], points[j]), i, j)
        pq.put(tup)

count = 0
while pq.qsize() > 0 and count < 1000:
    dist, p1_i, p2_i = pq.get()
    if (p1_i not in g or p2_i not in g) or not sameCircuit(p1_i, p2_i):
        g.setdefault(p1_i, set()).add(p2_i)
        g.setdefault(p2_i, set()).add(p1_i)
    count += 1

res = 1
visited = set()
pq = PriorityQueue()
for i in range(3):
    pq.put(-1)
for i in g:
    count = 0
    if i not in visited:
        nodes = [i]
        visited.add(i)
        while len(nodes):
            node = nodes.pop()
            count += 1
            for new_node in g[node]:
                if new_node not in visited:
                    visited.add(new_node)
                    nodes.append(new_node)
    if count > 0:
        low = pq.get()
        pq.put(max(low, count))

res = 1
while pq.qsize() > 0:
    res *= pq.get()
print(res)
            