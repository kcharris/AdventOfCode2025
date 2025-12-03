f = open("Day3\data.txt")
res = 0
for line in f.readlines():
    arr = [int(c) for c in line.strip()]
    m1 = max(arr[:len(arr)-1])
    r = 0
    while arr[r] != m1:
        r += 1
    r += 1
    m2 = 0
    while r < len(arr):
        m2 = max(m2, arr[r])
        r += 1
    
    res += m1*10 + m2

print(res)