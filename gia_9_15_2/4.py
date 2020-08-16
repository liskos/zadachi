# 4-ая задача
import sys

sys.stdin = open(file='in/4.in', mode='r', encoding='utf-8')
sys.stdout = open(file='out/4.out', mode='w', encoding='utf-8')

chislo = int(input())
minimum3 = 30001
while chislo != 0:
    if (chislo % 3 == 0) and (chislo < minimum3):
        minimum3 = chislo
    chislo = int(input())
print(minimum3)

# исправил на верно
# совмещаются два алгоритма

# - нахождение минимального -

# цикл перебор элементов или перебор индекса
#     если введенный элемент < минимального
#         то минимальный заменяй на введенный элемент
#     введенный элемент = int(input()) новый элемент с клавиатуры

#     x = int(input())
#     while x != 0:
#         if x < minimum:
#             minimum = x
#         x = int(input())

#     for i in range(n):
#         x = int(input())
#         if x < minimum:
#             minimum = x


#  - нахождения элемента по свойствам -
# цикл перебор элементов или перебор индекса
#         if элемент подходит по свойству
#             считай его количество или сумму
#             или запоминай его в какой то переменной
#         считывай новый элемент с клавиатуры

#     x = int(input())
#     while x != 0:
#         if x % 2 == 0:
#             count += 1
#             summa += x
#         x = int(input())
