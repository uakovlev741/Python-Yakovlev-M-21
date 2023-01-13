empty = set()
duble = set()
k = 0
for i in range(int(input())):
 line = input()
 if line not in empty:
    empty.add(line)
 else:
    k += 1
 if line not in duble:
    duble.add(line)
k += len(duble)
print(k)