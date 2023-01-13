english_n = int(input())
german_n = int(input())
franch_n = int(input())
intersection = set()
first = set()
second = set()
third = set()
cout = 0
for _ in range(english_n + german_n + franch_n):
    name = input()
    if name in second:
        third.add(name)
    elif name in first:
        second.add(name)
    else:
        first.add(name)
difference = (len(second) - len(third))
if difference > 0:
    print(difference)
else:
    print("NO")