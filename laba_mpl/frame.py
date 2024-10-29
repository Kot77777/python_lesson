import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter

count = 0
x_data = []
y_data = []
with open('data_task_2.txt', 'r') as file:
    for line in file:
        if count % 2 == 0:
            line1 = list(map(float, line.split(' ')))
            x_data.append(line1)
        else:
            line2 = list(map(float, line.split(' ')))
            y_data.append(line2)
        count += 1
N = 6

# Функция для обновления графика
def update_plot(val):
    index = int(val)  # Получаем индекс из ползунка
    ax.clear()
    ax.plot(x_data[index], y_data[index])
    ax.set_title(f'Frame {index + 1}', fontsize = 14)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.minorticks_on()
    ax.set_ylim(-12, 12)
    canvas.draw()

root = tkinter.Tk()
root.title("Интерактивные графики")

fig, ax = plt.subplots(figsize=(20, 15))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

slider = tkinter.Scale(root, from_=0, to=N-1, orient=tkinter.HORIZONTAL,
                  label='Двигайте ползунок', font=(15), command=update_plot, length=400, sliderlength=60, width=50)
slider.pack(side=tkinter.BOTTOM)

update_plot(slider.get())

tkinter.mainloop()
