# 26-ая задача

import sys

sys.stdin = open(file='in/26.in', mode='r', encoding='utf-8')
sys.stdout = open(file='out/26.out', mode='w', encoding='utf-8')

chislo = int(input())
colichestvo = 0
while chislo != 0:
    if chislo % 6 == 0 and chislo % 10 == 4:
        colichestvo += 1
    chislo = int(input())
print(colichestvo)

# верно
