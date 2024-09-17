sp = list(map(int, input().split()))
for i in sp:
    if (sp.count(i) > 1):
        a = set(sp)
        a.remove(i)
    else:
        a = set(sp)
print(max(a))
