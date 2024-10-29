N = int(input())
chanel = []
u = []
for i in range(N):
    line = input()
    chanel_id_i, u_i = line.split(':', 1)
    chanel.append(chanel_id_i)
    u.append(set(list(map(int, u_i.split(', ')))))

bot = set(list(map(int, input().split(', '))))
u_new = []
for i in u:
     u_new.append(i - bot)

id = int(input())
large = 0
j = 0
for i in range(len(u_new)):
    if i != id - 1:
        A = u_new[i] - u_new[id - 1]
        B = u_new[id - 1] - u_new[i]
        C = u_new[i] | u_new[id - 1]
        J = len(C) / (len(A) + len(B) + len(C))
        if J > large:
            large = J
            j = i

print(j + 1)
