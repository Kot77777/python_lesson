N = int(input())
set_colors = set()
for i in range(N):
    line = input()
    name, colors = line.split(';', 1)
    color_new = [color.strip().lower() for color in colors.split(',')]
    set_colors.update(color_new)
print(', '.join(sorted(set_colors)))