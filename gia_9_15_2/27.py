# 27-ая задача

import sys

sys.stdin = open(file='in/27.in', mode='r', encoding='utf-8')
sys.stdout = open(file='out/27.out', mode='w', encoding='utf-8')

chislo = int(input())
symma_chisel = 0
while chislo != 0:
    if chislo % 6 == 0 or chislo % 11 == 0:
        symma_chisel += chislo
    chislo = int(input())
print(symma_chisel)

# верно, поправил
