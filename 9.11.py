n = int(input())
list1 = []
for i in range(n):
    b = input()
    list1.append(b)
m = int(input())
list2 = []
for i in range(m):
    v = input()
    list2.append(v)
for i in list2:
    if i in list1:
        print(i)
