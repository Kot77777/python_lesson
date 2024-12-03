import numpy as np

[N, M] = list(map(int, input().split()))

pole = []
for i in range(N):
    pole.append(list(map(int, input().split())))

pole_np = np.array(pole)
mask = (pole_np < -5)
print(np.sum(mask))

mask1 = -1*(pole_np < 0)*pole_np
print(np.sum(mask1))
print(np.max(pole_np))