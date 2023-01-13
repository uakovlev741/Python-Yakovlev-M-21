a = int(input())
list1 = []
for i in range(a):
    list1.append(input())
b = int(input())
list2 = []
for i in range(b):
    list2.append(input())
list3 = []
for i in range(a):
    f = 0
    for k in range(b):
        if list1[i].find(list2[k]) == -1:
            f = 1
            break
    if f == 0:
        list3.append(list1[i])
print("\n".join(list3))
