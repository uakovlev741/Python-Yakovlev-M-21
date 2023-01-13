n = int(input())
list = []
for i in range(n):
    m = int(input())
    list.append(m)
for i in range(n - 1):
    print(list[i] + list[i + 1])
