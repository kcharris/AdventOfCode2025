f = open("Day3\data.txt")
def getIndexOfMax(l, r):
    m_found = -1
    idx = -1
    for i in range(l, r):
        if m_found < arr[i]:
            m_found = arr[i]
            idx = i
    return idx

res = 0
for line in f.readlines():
    arr = [int(c) for c in line.strip()]
    max_arr = [-1]
    for i in range(0,12):
        l = max_arr[-1] + 1
        r = len(arr) - (11-i)
        j = getIndexOfMax(l, r)
        max_arr.append(j)
    pwr = 0
    while pwr < 12:
        res += 10**pwr * arr[max_arr.pop()]
        pwr += 1

print(res)