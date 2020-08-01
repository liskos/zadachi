N = 30
a = []
for i in range(N):
    a.append(int(input()))
maximum = a[0]
count_max = 1
for i in range(1, N):
    if a[i] > maximum:
        maximum = a[i]
        count_max = 1
    elif a[i] == maximum:
        count_max += 1
print(count_max)
