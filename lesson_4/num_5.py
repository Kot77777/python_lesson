file = input()
key = input()
sp = []
count = 0
try:
    with open(file, 'r') as f:
        sp += f.read().split()
    for i in sp:
        if i.upper() == key.upper():
            count += 1
    print(count)
except FileNotFoundError:
    print(count)

