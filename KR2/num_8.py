import numpy as np

[N, M, K] = list(map(int, input().split()))
sp1 = []
sp1.append(['.'] * (M + 2))
for i in range(1, N + 1):
    row = input()
    sp1.append(['.'] + list(row) + ['.'])

sp1.append(['.'] * (M + 2))
sp = np.array(sp1)
predicted_sp = sp.copy()



ind = [[-1, -1], [-1, 0], [-1, 1],
       [0, -1], [0, 1],
       [1, -1], [1, 0], [1, 1]]

for _ in range(K):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if sp[i][j] == '#':
                k = 0
                for l in ind:
                    if sp[i+l[0]][j+l[1]] == '#':
                        k += 1
                    if k >= 4:
                        predicted_sp[i][j] = '.'
                        break
                if k < 2:
                    predicted_sp[i][j] = '.'
            if sp[i][j] == '.':
                k = 0
                for l in ind:
                    if sp[i + l[0]][j + l[1]] == '#':
                        k += 1
                    if k > 3:
                        predicted_sp[i][j] = '.'
                        break
                if k == 3:
                    predicted_sp[i][j] = '#'
    sp = predicted_sp.copy()
for i in range(1, N+1):
    for j in range(1, M+1):
        print(sp[i][j], end='')
    print('\n')




