n=int(input())
l=[]
v=input().split()
for x in v:
    if x not in l:
        l.append(x)
l=[int(x) for x in l]
l.sort()
print(l[-2])
