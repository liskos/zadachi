# 81-ая задача

import sys

sys.stdin = open(file='in/81.in', mode='r', encoding='utf-8')
sys.stdout = open(file='out/81.out', mode='w', encoding='utf-8')

n = int(input())
maximum = 0  # в последовательности натуральных чисел это минимальное значение
for i in range(n):
    chislo = int(input())
    if chislo % 10 == 2 and chislo > maximum:
        maximum = chislo
print(maximum)

# исправил на верно, в таких задачах массивы излишни
