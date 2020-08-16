# 93-ая задача

import sys as s

s.stdin = open(file='in/8.in', mode='r', encoding='utf-8')
s.stdout = open(file='out/8.out', mode='w', encoding='utf-8')

chislo = 1
col_chisel = 0
while chislo != 0:
    chislo = int(input())
    if chislo % 6 == 0 and chislo % 10 == 4:
        col_chisel += 1
print(col_chisel)
