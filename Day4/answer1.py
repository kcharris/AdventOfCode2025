f = open("Day4\data.txt")

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

for line in f.readlines():
    grid.append(line.strip())

res = 0
for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] == "@" and getRollCount(r, c) < 4:
            res += 1
print(res)