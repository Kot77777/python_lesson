sp = list(map(int, input().split()))
n = int(input())
sp.sort()
sp_new = sp[-n:]
for i in sp_new:
    print(i)
