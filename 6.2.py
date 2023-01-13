used = set()
num = int(input())
for i in range(num):
 line = input()
 used.add(line)
line = input()
if line in used:
 print('TRY ANOTHER')
else:
 print('OK')