import matplotlib.pyplot as plt
import numpy as np

sp = []
with open('students.csv', 'r') as file:
    for line in file:
        sp.append(line.split(';'))
print(sp)
prep = ['prep1', 'prep2', 'prep3', 'prep4', 'prep5', 'prep6', 'prep7']
group = ['751', '752', '753', '754', '755', '756']

mark_p = [[0 for i in range(7)] for j in range(8)]
mark_g = [[0 for i in range(6)] for j in range(8)]

for j in range(len(sp)):
    mark_p[int(sp[j][2]) - 3][prep.index(sp[j][0])] += 1

for j in range(len(sp)):
    mark_g[int(sp[j][2]) - 3][group.index(sp[j][1])] += 1


print(mark_p)

species_prep = (
    'prep1',
    'prep2',
    'prep3',
    'prep4',
    'prep5',
    'prep6',
    'prep7',
)
weight_counts_prep = {
    '3': np.array(mark_p[0]),
    '4': np.array(mark_p[1]),
    '5': np.array(mark_p[2]),
    '6': np.array(mark_p[3]),
    '7': np.array(mark_p[4]),
    '8': np.array(mark_p[5]),
    '9': np.array(mark_p[6]),
    '10': np.array(mark_p[7]),
}

species_group = (
    '751',
    '752',
    '753',
    '754',
    '755',
    '756',
)
weight_counts_group = {
    '3': np.array(mark_g[0]),
    '4': np.array(mark_g[1]),
    '5': np.array(mark_g[2]),
    '6': np.array(mark_g[3]),
    '7': np.array(mark_g[4]),
    '8': np.array(mark_g[5]),
    '9': np.array(mark_g[6]),
    '10': np.array(mark_g[7]),
}

width = 0.5

fig, ax = plt.subplots(2, 1, figsize=(15, 8))
bottom_p = np.zeros(7)
for boolean, weight_count in weight_counts_prep.items():
    p = ax[0].bar(species_prep, weight_count, width, label=boolean, bottom=bottom_p)
    bottom_p += weight_count
ax[0].set_title("Marks per prep")
ax[0].legend(loc="upper right")

bottom_g = np.zeros(6)
for boolean, weight_count in weight_counts_group.items():
    g = ax[1].bar(species_group, weight_count, width, label=boolean, bottom=bottom_g)
    bottom_g += weight_count
ax[1].set_title("Marks per group")
ax[1].legend(loc="upper right")

plt.savefig('Task_3.png', dpi=300)
plt.show()
