n = int(input())
list = []
for i in range(n):
    list.append(input())
m = input()
for i in list:
    if m in i:
        print(i)
