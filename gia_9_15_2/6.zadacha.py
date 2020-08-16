#28-ая задача

import sys as s

s.stdin = open(file = 'in/6.in', mode = 'r', encoding='utf-8')
s.stdout = open(file = 'out/6.out', mode = 'w', encoding='utf-8')

chislo = 1
symma_chisel = 0
while chislo != 0:
    chislo = int(input())
    if 1 < chislo < 10:
        symma_chisel += chislo
print(symma_chisel)