from functools import cache
f = open("Day10\data.txt")
M = 10**9+7

def findMinPresses(lights, buttons):
    target_mask = 0
    for i in range(len(lights)):
        target_mask = target_mask << 1
        if lights[i] == "#":
            target_mask += 1

    def applyButton(button, mask) -> int:
        for b in button:
            mask ^= 1 << (len(lights)-b-1)
        return mask

    @cache
    def helper(i, mask):
        if mask == target_mask:
            return 0
        if i >= len(buttons):
            return M
        
        
        left = 1 + helper(i+1, applyButton(buttons[i], mask))
        right = helper(i+1, mask)
        return min(left, right)
    return helper(0, 0)

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
    jolts = list(map(int, line[i+1:len(line)-1].split(",")))
    return lights, buttons, jolts

res = 0
for line in f.readlines():
    line = line.strip()
    lights, buttons, jolts = parseManualLine(line)
    res += findMinPresses(lights, buttons)

print(res)