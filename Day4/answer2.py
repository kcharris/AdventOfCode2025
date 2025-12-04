from sortedcontainers import SortedSet
import time
time_start = time.time()
f = open("Day4\data.txt")

removed = set()
roll_d = {}
ss = SortedSet()
grid = []
def isValid(r, c):
    if r < len(grid) and r >= 0 and c < len(grid[0]) and c >= 0:
        return True
    return False

def getRollCount(r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if isValid(r+i, c+j) and grid[r+i][c+j] == "@":
                    count += 1
    return count

def removeRollAndUpdateCounts(r,c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                r1, c1 = r+i, c+j
                if isValid(r1, c1) and grid[r1][c1] == "@" and (r1, c1) not in removed:
                    prev_count = roll_d[(r1, c1)]
                    roll_d[(r1, c1)] -= 1
                    ss.remove((-prev_count, r1, c1))
                    ss.add((-roll_d[(r1, c1)], r1, c1))

for line in f.readlines():
    grid.append(line.strip())

res = 0
for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] == "@":
            roll_count = getRollCount(r,c)
            roll_d[(r, c)] = roll_count
            ss.add((-roll_count, r, c))
            
while -ss[-1][0] < 4:
    res += 1
    _, r, c = ss.pop()
    removed.add((r, c))
    removeRollAndUpdateCounts(r, c)
time_end = time.time()
print(time_end - time_start)

print(res)