import sys

sys.stdin = open(file="in/25.in", mode="r", encoding="utf-8")

a = int(input())
b = int(input())

print((b - a + 1) // 2) if (b - a + 1) % 2 == 0 else print(((b - a + 1) + 1) // 2)
