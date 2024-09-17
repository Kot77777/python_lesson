sp = input().split()
dic = {}
for i in sp:
    dic[i] = sp.count(i)

lst = []
for i in dic:
    lst.append([i, dic[i]])

for i in range(len(lst) - 1):
    for j in range(i+1, len(lst)):
        if lst[i][1] < lst[j][1]:
            lst[i], lst[j] = lst[j], lst[i]

for i in range(len(lst) - 1):
    for j in range(i+1, len(lst)):
        if lst[i][0] > lst[j][0] and lst[i][1] == lst[j][1]:
            lst[i], lst[j] = lst[j], lst[i]

for i in lst:
    print(i[1], i[0])




