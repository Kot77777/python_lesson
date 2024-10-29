N = int(input())
sp = []
dict = {}
for i in range(N):
    sp += input().split()
sp_lower = []
for i in sp:
    sp_lower.append(i.lower())
for i in sp_lower:
    dict[i] = sp_lower.count(i)
sp = list(set(sp))
sp1 = []
for i in sp:
    sp1.append(i.upper())
sp3 = []
for i in range(len(sp1)):
    if(sp1.count(sp1[i]) > 2):
        sp3.append(sp[i])
sp4 = []
for i in sp3:
    sp4.append(i.lower())
sp4 = list(set(sp4))
dict1 = {}
for i in sp4:
    dict1[i] = dict[i]
dict2 = {}
for i in dict1:
    dict2[dict1[i]] = i
for i in sorted(dict2, reverse=True):
    print(dict2[i])

