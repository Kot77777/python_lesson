s = input()
count = 0

if '.' in s:
    for i in s:
        if (i == '.'):
            break
        count += 1
    n = len(s) - count - 1
    print(f"{(float(s) - 10**(-n)):.{n}f}")
else:
    print(int(s) - 1)