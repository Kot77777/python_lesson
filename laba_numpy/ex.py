N = int(input().strip())
points = []

for _ in range(N):
    x, y, brightness = map(int, input().strip().split())
    points.append((x, y, brightness))

filtered = {}
for point in points:
    x, y, brightness = point
    distance_squared = x * x + y * y  

    if brightness >= 10 and distance_squared <= 100:
        if point in filtered:
            filtered[point] += 1
        else:
            filtered[point] = 1

final_points = [(x, y, brightness) for (x, y, brightness), count in filtered.items() if count >= 2]
final_points.sort(key=lambda p: (-p[2], -filtered[p], (p[0]**2 + p[1]**2)))

for x, y, brightness in final_points:
    print(f"{x} {y} {brightness}")
