import numpy as np

[N, M] = list(map(int, input().split()))
K = int(input())
sp = []
for i in range(K):
    sp.append(list(map(int, input().split())))
sp1 = np.array(sp)
pole = np.zeros((N, M))

for i in sp1:
    pole[:, i[1]] += 1
    pole[i[0], :] += 1
k = 0
for i in range(N):
    for j in range(M):
        if pole[i][j] > 1:
            k+=1
print(k)