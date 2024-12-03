import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Загружаем данные из файла
data = []
with open('1.txt', 'r') as file:
    for line in file:
        vector = list(map(float, line.split()))
        data.append(vector)

# Преобразуем список в numpy массив
data = np.array(data)
print(data)

# Проверяем размерность данных
if data.shape[1] < 3:
    raise ValueError("Недостаточно данных для построения графика (необходимы хотя бы 3 столбца).")

# Извлекаем данные
x = data[:, 4]
y = data[:, 5]
z = data[:, 6]

# Если ваши данные не образуют сетку, используйте scatter вместо plot_surface
# Например, если x и y не образуют равномерную сетку, используйте:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')  # Используем scatter для произвольных точек

# Настраиваем метки осей
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Показываем график
plt.show()
