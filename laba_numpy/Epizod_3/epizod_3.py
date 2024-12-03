import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

A = np.zeros((50, 50))
for i in range(len(A)):
    for j in range(len(A)):
        if i == j:
            A[i][j] = 1.
        if i - 1 == j:
            A[i][j] = -1.
A[0][49] = -1.

def create_window(data):
    fig, ax = plt.subplots()
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.minorticks_on()
    ax.set_ylim(0, 10)
    ax.set_xlim(0, len(data) - 1)
    ax.set_title("u(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("u(x)")
    return fig, ax

def step(u_i):
    u_next = u_i - 0.5 * np.dot(A, u_i)
    return u_next

def update(frame, u_states, line):
    x_coords = np.arange(len(u_states[frame]))
    line.set_data(x_coords, u_states[frame])
    return line,

u_0 = np.loadtxt('u_0.txt')
u = [u_0]
for i in range(1, 256):
    u.append(step(u[i - 1]))

fig, ax = create_window(u_0)
line, = ax.plot([], [], color='g')

anim = FuncAnimation(fig, update, fargs=(u, line),
                     frames=len(u), interval=50, blit=True)

anim.save('u_evolution.gif', writer='pillow', fps=10)
plt.show()
