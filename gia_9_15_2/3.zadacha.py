#50-ая задача
import sys as s


s.stdin = open(file='in/3.in', mode='r', encoding='utf-8')
s.stout = open(file='out/3.out', mode='w', encoding='utf-8')

shesterki = []
sravn = [1]
chislo = 1
while chislo != 0:
    chislo = int(input())
    if chislo % 10 == 6:
        shesterki.append(chislo)
if shesterki > sravn:
    minimum_chislo = min(shesterki)
    print(minimum_chislo)
else:
    print("Таких числ нет")
