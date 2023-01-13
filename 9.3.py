n = int(input())
list = []
for i in range(n):
    list.append(input())
m = int(input())
for i in list:
    if m <= len(i):
        print(i[m - 1], end="")
