s = input().split()
total = 0
for part in s:
    try:
        number = int(part)
        total += number
    except ValueError:
        continue
print(total)
