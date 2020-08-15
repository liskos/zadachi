# 20-ая задача

import sys as s

s.stdin = open(file="in/4.in", mode='r', encoding="utf-8")
s.stout = open(file="out/4.out", mode='w', encoding="utf-8")

chislo = 1
colychestvo = 0
while chislo != 0:
    chislo = int(input())
    if chislo % 4 == 0 and chislo % 10 == 2:
        colychestvo += 1
