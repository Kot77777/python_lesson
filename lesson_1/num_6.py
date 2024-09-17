N = int(input())
while N // 10 != 0:
    total = 0
    while N != 0:
        total += N % 10
        N //= 10
    N = total

else:
    total = N

print(total)