# 93-ая задача

import sys as s

s.stdin = open(file='in/8.in', mode='r', encoding='utf-8')
s.stdout = open(file='out/8.out', mode='w', encoding='utf-8')
col_chisel = 0
сol_chift = int(input())
for _ in range(сol_chift):
    chislo = int(input())
    if chislo % 6 == 0 and chislo % 10 == 4:
        col_chisel += 1
print(col_chisel)
