#27-ая задача
import sys as s
stdin = open(file='in/10.in', mode='r', encoding='utf-8')
stdout = open(file='out/10.out', mode='w', encoding='utf-8')

chislo = 1
symma_chisel = 0
while chislo != 0:
    chislo = int(input())
    if chislo % 6 == 0 or chislo % 11 == 0:
        symma_chisel += chislo
print(symma_chisel)