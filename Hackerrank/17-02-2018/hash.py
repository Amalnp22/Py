n=input()
inp_line=input()
inp_list=inp_line.split()
inp_list=[int(x) for x in inp_list]
t=tuple(inp_list)
print(hash(t))
