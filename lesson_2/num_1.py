n = int(input())
sp = [0, 1]
for i in range(2, n): sp.append(sp[i-2] + sp[i-1])
print(sp[len(sp)-1] if n!= 1 else 0)