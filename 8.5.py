a = int(input())
for i in range(a):
 line = str(input())
 if line[0] == "Н" and line[1] == "е":
    print(line[2:])
 else:
    print(line)
