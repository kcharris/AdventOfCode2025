from bisect import bisect_left
f = open("Day5\data.txt")

input_str = f.readline().strip()
ranges = []
while input_str != "":
    start, end = map(int, input_str.split("-"))
    ranges.append([start, end])
    input_str = f.readline().strip()

ranges.sort()
placeholder = []

while len(ranges) > 1:
    curr_range = ranges.pop()
    prev_range = ranges[-1]

    curr_s, curr_e = curr_range
    prev_s, prev_e = prev_range
    if prev_e >= curr_s or prev_s == curr_s:
        ranges[-1] = [prev_s, max(prev_e, curr_e)]
    elif prev_e < curr_s:
        placeholder.append(curr_range.copy())
        continue
    
placeholder.append(ranges.pop())
ranges = placeholder[::-1]

# print(ranges)
res = 0
for line in f.readlines():
    id = int(line)

    idx = bisect_left(ranges, id, key = lambda a: a[1])
    # print(id, idx)
    if idx >= 0 and idx < len(ranges) and id >= ranges[idx][0] and id <= ranges[idx][1]:
        res += 1

print(res)

