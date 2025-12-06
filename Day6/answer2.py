from functools import reduce
f = open("Day6\data.txt")

arr_in = []
for line in f.readlines():
    arr_in.append(line.strip("\n"))

def do_math(start, end):
    res = [[0 for _ in range(end-start)] for _ in range(len(arr_in))]
    for r in range(len(arr_in)-1):
        for c in range(start, end):
            res_c = c-start
            if arr_in[r][c] != " ":
                res[r+1][res_c] = res[r][res_c] * 10 + int(arr_in[r][c])
            else:
                res[r+1][res_c] = res[r][res_c]
    if arr_in[-1][start] == "+":
        return sum(res[-1])
    return reduce(lambda ans, x: ans * x, res[-1], 1)

math_lens = []
start = 0
for i in range(1, len(arr_in[0])):
    if arr_in[-1][i] in ["+", "*"]:
        math_lens.append([start, i-1])
        start = i
math_lens.append([start, len(arr_in[0])])

res = 0
for start, end in math_lens:
    res += do_math(start, end)

print(res)