n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(i +-1):
    for j in range(len(a) - 1 - i):
        v = (len(a[j]), a[j])
        b = (len(a[j + 1]), a[j + 1])
        if v > b:
            a[j], a[j + 1] = a[j + 1], a[j]
for s in a:
    print(s)
