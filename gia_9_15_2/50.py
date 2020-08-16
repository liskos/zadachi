# 50-ая задача
import sys

sys.stdin = open(file='in/50.in', mode='r', encoding='utf-8')
sys.stdout = open(file='out/50.out', mode='w', encoding='utf-8')

n = int(input())
minimum = 30001
for _ in range(n):
    chislo = int(input())
    if chislo % 10 == 6 and chislo < minimum:
        minimum = chislo
if minimum == 30001:
    minimum = "Таких цифр нет"
print(minimum)
#  исправил на как надо
