import matplotlib.pyplot as plt
Num = []
coordinates_full = []
for i in range(1, 6):
    with open(f'dead_moroz/00{i}.dat', 'r') as file:
        N = int(file.readline().strip())
        Num.append(N)
        x = []
        y = []
        for _ in range(N):
            line = file.readline().strip()
            x_i, y_i = map(float, line.split())
            x.append(x_i)
            y.append(y_i)
        coordinates_full.append([x, y])


fig, ax = plt.subplots(3, 2, figsize=(10, 8))

fig.subplots_adjust(wspace=0.5, hspace=0.5)
for i in range(5):
    ax[i // 2, i % 2].set_title(f'Number of points {Num[i]}', fontsize=12)
    ax[i//2, i%2].scatter(coordinates_full[i][0], coordinates_full[i][1], s = 7, c = 'g')
    ax[i//2, i%2].set_aspect('equal', adjustable='box')
    ax[i//2, i%2].grid(True, which='both', linestyle='--', linewidth=0.5)
    ax[i//2, i%2].minorticks_on()
fig.suptitle('Визуализация данных', fontsize=16)
fig.delaxes(ax[2, 1])
plt.savefig('Task_1.png', dpi=300)
plt.show()



