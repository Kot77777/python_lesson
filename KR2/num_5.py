import numpy as np

N = int(input())
u_before = np.array(list(map(float, input().split())))
sp = []
for i in range(N):
    sp.append(list(map(float, input().split())))

R = np.array(sp)
K = int(input())
for i in range(K):
    u_before = np.dot(R, u_before)

for value in u_before:
    print(f"{value:.4f}", end=' ')