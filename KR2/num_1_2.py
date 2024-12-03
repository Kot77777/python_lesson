s = input().split()
sp = []
for i in s:
    sp.append(i.lower())
print(len(set(sp)))