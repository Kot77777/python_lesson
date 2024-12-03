import numpy as np

def f(stud, ex):
    total = 0
    for i in ex:
        dif = (stud - i) / 10
        S = 1 / (1 + np.exp(-dif))
        total += S
    if total >= 0.5*len(ex):
        return True
    else: return False

student = list(map(int, input().split()))
exercise = list(map(int, input().split()))
tot = 0
for i in student:
    tot += f(i, exercise)

print(tot)