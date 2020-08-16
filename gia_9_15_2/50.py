# 50-ая задача
import sys as s

s.stdin = open(file='in/50.in', mode='r', encoding='utf-8')
s.stout = open(file='out/50.out', mode='w', encoding='utf-8')

shesterki = []
sravn = [1]
col_chifr = int(input())
for _ in range(col_chifr):
    chislo = int(input())
    if chislo % 10 == 6:
        shesterki.append(chislo)
if sravn > shesterki:
    "Таких цифр нет"
else:
    Minimum_6 = min(shesterki)
    print(Minimum_6)
#  неверно, делается через цикл for, нет в конце нуля,  и без функции min
