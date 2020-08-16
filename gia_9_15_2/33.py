# задача 33
import sys as s

s.stdin = open(file='in/33.in', mode='r', encoding="utf-8")
s.stdout = open(file='out/33.out', mode='w', encoding="utf-8")

chislo = 1
sym = 0
while chislo != 0:
    chislo = int(input())
    if chislo % 4 == 0 or chislo % 9 == 0:
        sym += chislo
print(sym)

# верно
