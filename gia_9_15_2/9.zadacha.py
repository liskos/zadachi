# 4-ая задача
import sys as s

# s.stdin = open(file='in/9.in', mode='r', encoding='utf-8')
# s.stdin = open(file='out/9.out', mode='w', encoding='utf-8')

chislo = 1
chisla_ok_na_3 = []
while chislo != 0:
    chislo = int(input())
    if chislo % 10 == 3:
        chisla_ok_na_3.append(chislo)
Min_3 = min(chisla_ok_na_3)
print(Min_3)