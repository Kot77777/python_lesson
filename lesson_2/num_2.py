n = int(input())
sp = [0, 0, 0, 0, 0, 0, 0, 0, 1]
for i in range(9, n): sp.append(sum([sp[i-j] for j in range(1, 10)]))
print(sp[n-1] if n!= 1 else 0)
