import sys

sys.stdin = open(file="in/4.in", mode="r", encoding="utf-8")

a = []
for i in range(10):
    a.append([])
    x = input().split()
    for j in range(20):
        a[i].append(int(x[j]))
minimum = 0
number_min = 1
for i in a[0]:
    minimum += i
for i in range(10):
    summa = 0
    for j in range(20):
        summa += a[i][j]
    if summa < minimum:
        minimum = summa
        number_min = i + 1
print(number_min)
