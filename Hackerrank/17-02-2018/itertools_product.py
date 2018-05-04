import itertools
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in itertools.product(a,b):
    print(i, end=' ')
