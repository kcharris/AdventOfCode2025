f = open("Day6\data1.txt")

arr = []
for line in f.readlines():
    arr.append(line.strip().split())
    # print(arr)
    if arr[-1][0] not in ["*", "+"]:
        arr[-1] = list(map(int, arr[-1]))

res_arr = [arr[0][i] for i in range(len(arr[0]))]
for r in range(1, len(arr)-1):
    for c in range(len(arr[r])):
        if arr[-1][c] == "+":
            res_arr[c] += arr[r][c]
        else:
            res_arr[c] *= arr[r][c]

print(sum(res_arr))


