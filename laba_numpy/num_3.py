import numpy as np

# path1 = input()
# path2 = input()
X = np.array(list(map(np.float64, input().split())), dtype=np.float64)

A = np.loadtxt("1.txt", np.float64)
B = np.loadtxt("2.txt", np.float64)

A2 = np.dot(A, A)
step_1 = np.dot(X, A2)
step_2 = np.dot(step_1, B)
print(step_2)