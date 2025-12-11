from functools import cache
def parseLine(line):
    line = line.strip()
    i = 0
    while line[i] != ":":
        i += 1
    node = line[:i]
    i += 1
    next_nodes = line[i:].split()
    return node, next_nodes

def solve(f):
    graph = {}
    for line in f.readlines():
        node, next_nodes = parseLine(line)
        graph.setdefault(node, next_nodes)

    visited = set()
    def dfsPathCount(node):
        if node == "out" and visited.issuperset({"fft", "dac"}):
            return 1
        if node not in graph:
            return 0
        
        res = 0
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                res += dfsPathCount(n)
                visited.remove(n)
        return res
    
    return dfsPathCount("svr")

f = open("Day11\data2.txt")
data1_answer = 2
answer1 = solve(f)
print(f"Test answer is {answer1}. Test expected is {data1_answer}")

if answer1 == data1_answer:
    f = open("Day11\data.txt")
    print(solve(f))
