f = (open(input(), 'r').read()).split()
v = [len(i) for i in f]
print(f[v.index(max(v))])
