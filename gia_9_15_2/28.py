# 28-ая задача

import sys

sys.stdin = open(file='in/28.in', mode='r', encoding='utf-8')
sys.stdout = open(file='out/28.out', mode='w', encoding='utf-8')

chislo = int(input())
symma_chisel = 0
while chislo != 0:
    if (0 < chislo < 10) and (chislo % 3 == 0):
        symma_chisel += chislo
    chislo = int(input())
print(symma_chisel)

# не верно, надо сумма однозначных чисел, кратных трем
# было 1 < chislo < 10
# стало (0 < chislo < 10) and (chislo % 3 == 0)

