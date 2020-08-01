N = 30
a = []
for i in range(N):
    a.append(int(input()))
number = 0
max_summa = a[0] + a[1] + a[2]
for i in range(1, N-2):
    summa = a[i] + a[i+1] + a[i+2]
    if summa > max_summa:
        max_summa = summa
        number = i
print(a[number], a[number+1], a[number+2])
