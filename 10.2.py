n = int(input())
names = list()
for i in range(n):
    names.append(input())
for j in names:
    print(j)
print()
for j in names:
    if int(j[-1]) > 3:
        print(j)
