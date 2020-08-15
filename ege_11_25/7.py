# допускается также
# использовать две
# целочисленные переменные x и y
# и вещественную переменную s
import sys
sys.stdin = open(file="in/7.in", mode="r", encoding="utf-8")
n = 30
a = [0] * n
for i in range(n):
    a[i] = int(input())
x = 0
s = 0
for i in a:
    if i > 20:
        s += i
        x += 1
print(s / x)
