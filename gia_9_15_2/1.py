import sys

sys.stdin = open(file="in/1.in", mode="r", encoding="utf-8")
sys.stdout = open(file="out/1.out", mode="w", encoding="utf-8")

a = int(input())
b = int(input())

print((b - a + 1) // 2) if (b - a + 1) % 2 == 0 else print(((b - a + 1) // 2) + 1)
