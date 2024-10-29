N = int(input())
sp = []
for i in range(N):
    sp.append(list(map(int, input().split())))

large = 0
k = 0

for i in range(len(sp)):
    if(sum(sp[i]) > large):
        large = sum(sp[i])
        k = i
sp[k].sort(reverse=True)
print(*sp[k])