# Номер 25
import sys as s

s.stdin = open(file='in/25.in', mode='r', encoding="utf-8")
s.stout = open(file='out/25.out', mode='w', encoding="utf-8")

chislo = 1
col = 0
while chislo != 0:
    chislo = int(input())
    sotni = chislo // 100
    if 1 <= sotni < 10:
        if chislo % 4 == 0:
            col += 1
print("Всего таких чисел - {}".format(col))

# верно
