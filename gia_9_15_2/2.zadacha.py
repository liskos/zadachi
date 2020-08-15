#задача 33
import  sys as s


s.stdin = open( file='in/2.in', mode='r', encoding="utf-8")
s.stout = open( file='out/2.out', mode='w', encoding="utf-8")

chislo = 1
sym = 0
while chislo != 0:
    chislo = int(input())
    if chislo % 4 == 0 or chislo % 9 == 0:
        sym += chislo
print(sym)