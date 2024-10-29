N, M = map(int, input().split())
pole = []
for i in range(M):
    pole.append(list(map(int, input().split())))
K = int(input())
robot = []
for i in range(K):
    robot.append(list(map(int, input().split())))
total = 0
pole_update = [[0] * N for i in range(M)]
for i in range(len(robot)):
    for y in range(M):
        for x in range(N):
            if max(abs(x - robot[i][0]), abs(y - robot[i][1])) <= robot[i][2] and pole_update[y][x] == 0:
                total += pole[y][x]
                pole_update[y][x] = 1
print(total)