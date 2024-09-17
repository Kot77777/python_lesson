from pathlib import Path
sp = []
for i in input().split():
    file_path = Path(i)
    if file_path.is_file():
        with open(i, 'r') as f:
            sp += f.read().split()
sp1 = list(set(sp))
sp1.sort()
print(*sp1)