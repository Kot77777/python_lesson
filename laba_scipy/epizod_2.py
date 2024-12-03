import matplotlib.pyplot as plt
from scipy import linalg
import numpy as np


with open("system.txt", "r") as f:
    n = int(f.readline().strip())
    A = np.zeros((n, n))
    for i in range(n):
        a_line = f.readline().strip()
        A_values = list(map(float, a_line.split()))
        A[i] = A_values
    b_line = f.readline().strip()
    b_values = list(map(float, b_line.split()))
    b = np.array(b_values)

x = linalg.solve(A, b)

plt.bar(range(len(x)), x, color='blue')
plt.title('Решение системы линейных уравнений')
plt.xlabel('Индекс переменной')
plt.ylabel('Значение переменной')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.minorticks_on()
plt.savefig('Epizod_2.png', dpi=300)
plt.show()
