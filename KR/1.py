K = int(input())
N = int(input())
large = 0
total = 0
for i in range(N):
    into, out = map(int, input().split())
    total += out - into
    large = max(large, total - K)
print(large)

