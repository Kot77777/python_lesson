file = input()
sp1 = []
sp2 = []
large = float('-inf')
small = float('inf')
s = 0
l = 0
try:
    with open(file, 'r') as f:
        sp = (f.read().split('\n'))
    for i in sp:
        if i.strip():
            sp1.append(list(map(int, i.split(';')[1:])))
            sp2.append(i.split(';'))
    for i in range(len(sp1)):
        if(sum(sp1[i]) > large):
            l = i
            large = sum(sp1[i])

        if(sum(sp1[i]) <= small):
            s = i
            small = sum(sp1[i])


except (FileNotFoundError, IOError):
    print("no data")
    exit()
print(sp2[l][0], large)
print(sp2[s][0], small)