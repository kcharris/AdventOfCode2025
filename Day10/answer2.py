from functools import cache
f = open("Day10\data.txt")
M = 10**9+7

def findMinPresses(buttons, jolts):
    def applyButton(button, j_tup) -> tuple:
        res_j = list(j_tup)
        for b in button:
            res_j[b] += 1
        return tuple(res_j)
    
    def isOverJolt(j_tup):
        for i in range(len(jolts)):
            if j_tup[i] > jolts[i]:
                return True
        return False

    @cache
    def helper(j_tup):
        if j_tup == jolts:
            return 0
        if isOverJolt(j_tup):
            # print(j_tup, jolts)
            return M
        
        res = M
        for i in range(len(buttons)):
            new_j_tup= applyButton(buttons[i], j_tup)
            res = min(res, 1 + helper(new_j_tup))
        return res
    res = helper(tuple(0 for _ in range(len(jolts))))
    return res

def parseManualLine(line):
    lights = []
    buttons = []

    # get lights
    i = 1
    while line[i] != "]":
        lights.append(line[i])
        i += 1
    # get buttons
    i += 1
    while line[i] != "{":
        if line[i] == "(":
            r = i+1
            while line[r] != ")":
                r += 1
            buttons.append(list(map(int, line[i+1:r].split(","))))
            i = r
        i += 1
    # get jolts
    jolts = tuple(map(int, line[i+1:len(line)-1].split(",")))
    return lights, buttons, jolts

res = 0
for line in f.readlines():
    line = line.strip()
    lights, buttons, jolts = parseManualLine(line)
    res += findMinPresses(buttons, jolts)

print(res)