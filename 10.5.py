n = int(input())
a = []
for i in range(n):
    a.append(input())
b = int(input())
m = int(input())
for j in range(m):
    del a[b - 1::b]
print("\n".join(a))
