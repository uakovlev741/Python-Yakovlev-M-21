n = int(input())
s = ''
for x in range(1, n + 1):
    a = input()
    if a.find('cat') != -1:
        s += str(x) + ' ' + str(a.find('cat') + 1) + '\n'
print(s)