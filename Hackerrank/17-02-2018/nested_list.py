n = [[input(), float(input())] for i in range(int(input()))]
s = sorted(set([x[1] for x in n]))
if len(s) > 1:
    for name in sorted(x[0] for x in n if x[1] == s[1]):
        print(name)
