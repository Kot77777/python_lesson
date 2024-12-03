import numpy as np

[N, M] = list(map(int, input().split()))
K = int(input())
sp = []
for i in range(K):
    sp.append(list(map(int, input().split())))

sp_np = np.array(sp)
total = 0
for i in range(N):
    for j in range(M):
        if not(np.any((np.hstack(abs(sp_np[:, 0] - i) <= sp_np[:, 2]) * (abs(sp_np[:, 1] - j) <= sp_np[:, 2])))):
            total+=1
print(total)
