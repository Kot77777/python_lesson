import numpy as np
import matplotlib.pyplot as plt

for j in range(1, 4):
    data = np.loadtxt(f'signal0{j}.dat')
    print(data)

    update_data = []
    for i in range(len(data)-1):
        if i < 9:
            update_data.append(np.sum(data[0:i+1]) / (i + 1))

        else:
            update_data.append(np.sum(data[i-9:i+1]) / 10)

    new_data = np.array(update_data)
    print(new_data)
    fig, ax = plt.subplots(1, 2, figsize=(10, 8))
    ax[0].plot(data)
    ax[0].set_title('Сырой сигнал')
    ax[0].grid(True, which='both', linestyle='--', linewidth=0.5)
    ax[0].minorticks_on()

    ax[1].plot(new_data)
    ax[1].set_title('После фильтра')
    ax[1].grid(True, which='both', linestyle='--', linewidth=0.5)
    ax[1].minorticks_on()

    plt.savefig(f'{j}_array', dpi=300)
    plt.show()
    update_data.clear()