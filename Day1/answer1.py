f = open("Day1\data.txt")
res = 0
curr = 50
for line in f.readlines():
    letter, num = line[0], int(line[1:])
    if letter == "L":
        num *= -1
    curr = (curr + num) % 100
    if curr == 0:
        res += 1

print(res)
    
