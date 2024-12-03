import math

sp = list(map(int, input().split()))
K = int(input())

M = math.ceil(len(sp) * K / 100)
sp.sort()
print(sp[M-1])