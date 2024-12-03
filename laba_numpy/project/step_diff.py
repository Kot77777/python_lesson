import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("data.txt")
x = np.log(data[:, 0])
y = np.log(data[:, 1])

coef = np.polyfit(x[:-1], y[:-1], 1)
f = np.poly1d(coef)
print(coef)
print(f)

plt.scatter(x[:-1], y[:-1])
plt.xlabel("log(step)")
plt.ylabel("log(max_dif)")
plt.grid(True, which='both', linestyle='--', linewidth=0.2)
plt.minorticks_on()
plt.savefig("График", dpi = 300)
plt.show()

