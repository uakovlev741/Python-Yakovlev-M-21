a = input()
b = input()
bulls = 0
cows = 0
for i in range(0, len(a)):
 if a[i] == b[i]:
    bulls += 1
for i in range(0, len(a)):
 for j in range(0, len(b)):
    if i != j and a[i] == b[j]:
        cows += 1
print(bulls, cows, sep=" ")