animal = input().split()
human = input().split()
human_starts = set(name[0] for name in human)
unowned_animals = []
for animal in animal:
    if animal[0] not in human_starts:
        unowned_animals.append(animal)
unowned_animals.sort()
print(" ".join(unowned_animals))