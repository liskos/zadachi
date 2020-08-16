#81-ая задача

import sys as s

s.stdin = open(file = 'in/7.in', mode = 'r', encoding='utf-8')
s.stdout = open(file = 'out/7.out', mode = 'w', encoding='utf-8')

chisla_okanchi_na_2 = []
col_chifr = int(input())
for i in range (col_chifr):
    chislo = int(input())
    if chislo % 10 == 2:
        chisla_okanchi_na_2.append(chislo)
Maximum_na_2 = max(chisla_okanchi_na_2)
print(Maximum_na_2)
