# 26-ая задача

import sys as s

s.stdin = open(file='in/26.in', mode='r', encoding='utf-8')
s.stdout = open(file='out/26.out', mode='w', encoding='utf-8')

chislo = 1
colichestvo = 0
while chislo != 0:
    chislo = int(input())
    if chislo % 6 == 0 and chislo % 10 == 4:
        colichestvo += 1

print(colichestvo)

# верно
