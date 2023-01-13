n = int(input())
q = int(input())
print(0)
for i in range(0, n+1):
    a = int(input())
    if a > q:
        print('>')
    elif a < q:
        print('<')
    else:
        print(0)
    q = (q * i + a) / (i + 1)
