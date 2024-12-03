import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_window():
    fig, ax = plt.subplots()
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.minorticks_on()
    ax.set_ylim(-12, 12)
    ax.set_xlim(0, 20)
    ax.set_title("Frame")
    return fig, ax

def update(frame, x_data, y_data, line):
    line.set_data(x_data[frame], y_data[frame])
    return line,

count = 0
x_data = []
y_data = []
with open('data_task_2.txt', 'r') as file:
    for line in file:
        if count % 2 == 0:
            line1 = list(map(float, line.split()))
            x_data.append(line1)
        else:
            line2 = list(map(float, line.split()))
            y_data.append(line2)
        count += 1

N = len(x_data[0])

fig, ax = create_window()
line, = ax.plot([], [], color='orange')

anim = FuncAnimation(fig, update, fargs=(x_data, y_data, line),
                     frames=len(x_data), interval=100, blit=True)

anim.save('u_evolution.gif', writer='pillow', fps=10)
plt.show()
