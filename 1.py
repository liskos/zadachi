import codecs
import sys

save_stdin = sys.stdin
sys.stdin = codecs.open("in/1-5.in", "r", "utf-8")

N = 30
x1 = int(input())
x2 = int(input())
maximum = x1 + x2
number = 1
for i in range(2, N):
    x1 = x2
    x2 = int(input())
    if x1 + x2 > maximum:
        maximum = x1 + x2
        number = i
print(number)
