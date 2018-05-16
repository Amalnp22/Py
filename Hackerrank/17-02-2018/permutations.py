from itertools import permutations
inp=input().split()
l=[''.join(i) for i in permutations(sorted(inp[0]),int(inp[1]))]
for i in l:
    print(i)
