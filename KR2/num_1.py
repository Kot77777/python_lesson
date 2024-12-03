sp = (list(map(int, input().split())))
large = float('-inf')
for i in sp:
    if sp.count(i) == 1 and i > large:
        large = i

print(large)