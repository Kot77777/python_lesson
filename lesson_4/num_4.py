s = input()
large = 0
count = 0

for i in s:
    if (i != '1'):
        large = max(large, count)
        count = 0
    else:
        count += 1
print(max(large, count))