f = open("Day7\data1.txt")

g = []
for line in f.readlines():
    g.append([c for c in line.strip()])

def getStart():
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == "S":
                return (r, c)
start = getStart()

def isValid(r, c):
    if r < len(g) and r >= 0 and c < len(g[0]) and c >= 0:
        return True
    return False

visited = set()
def fireLaser(r, c):
    if not isValid(r, c) or (r,c) in visited:
        return 0
    visited.add((r, c))

    if g[r][c] == "^":
        return 1 + fireLaser(r+1, c-1) + fireLaser(r+1, c+1)
    return fireLaser(r+1, c)

print(fireLaser(start[0], start[1]))


