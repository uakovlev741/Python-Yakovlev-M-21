first = set()
second = set()
a = input()
while a != '':
 first.add(a)
 a = input()
a = input()
while a != '':
 second.add(a)
 a = input()
intersection = first & second
if intersection:
 for i in intersection:
    print(i)
else:
 print('EMPTY')
