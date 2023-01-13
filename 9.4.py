n = int(input())
list = []
for i in range(n):
    c = input()
    list.append(c)
m = int(input())
list1 = []
for i in range(m):
    b = int(input())
    list1.append(list[b - 1])
print(*list1, sep="\n")
